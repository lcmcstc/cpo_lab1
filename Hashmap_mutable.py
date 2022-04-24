# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Variant_8: Dictionary based on hash-map, open address
import threading
from threading import Lock


class MyEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "{" + str(self.key) + ":" + str(self.value) + "}"

    def __eq__(self, other):
        a = self.key == other.key
        b = self.value == other.value
        if a & b:
            return True
        else:
            return False


class MyIter:
    def __init__(self, myDictionary):
        self.data = myDictionary
        self.index = 0

    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):
        x = self.index
        self.index += 1
        if self.data.top < x:
            raise StopIteration
        if self.data.que[x] is None:
            return None
        entry = MyEntry(self.data.que[x], self.data.get(self.data.que[x]))
        return entry


class MyDictionary:

    def __init__(self, size=0):
        self.size = size
        self.store = [i for i in range(2 * size)]
        self.keys = [i for i in range(2 * size)]
        # que is used to record the seq of inserts
        self.que = [i for i in range(size)]
        self.top = -1
        # init que、store、keys
        for i in range(size):
            self.que[i] = None
        for i in range(2 * size):
            self.store[i] = None
            self.keys[i] = None

    def __eq__(self, other):
        for i in range(len(self.que)):
            if self.que[i] is None:
                break
            else:
                a = self.que[i] == other.que[i]
                b = self.get(self.que[i]) == other.get(other.que[i])
                if a & b:
                    continue
                else:
                    return False
        return True

    def to_list(self):
        ret = [i for i in range(len(self.que))]
        for i in range(len(self.que)):
            if self.que[i] is None:
                break
            entry = MyEntry(self.que[i], self.get(self.que[i]))
            ret[i] = entry
        return ret

    def from_list(self, tlist):
        self.__init__(len(tlist))
        for entry in tlist:
            self.add(entry.key, entry.value)
        return self

    # model hash(modular arithmetic) :: f( key ) = key mod p ( p ≤ m )
    def compute_index(self, key):
        hash_value = hash(key)
        if hash_value < 0:
            hash_value = hash_value * -1
        return hash_value % self.size

    def delete_que_by_key(self, key):
        t = 0
        for i in range(self.size):
            if self.que[i] == key:
                t += 1
            if self.que[i] is None:
                break
            if i + 1 >= self.size:
                self.que[i] = None
                break
            self.que[i] = self.que[i + t]
        if t > 0:
            self.top -= 1

    # transform key to index
    # open address
    def find_index_by_key(self, key):
        index = self.compute_index(key)
        if self.keys[index] == key:
            return index
        else:
            index += 1
            while index < len(self.keys):
                if self.keys[index] == key:
                    return index
                if self.keys[index] is None:
                    return -1
                index += 1
            return -1

    def add(self, key, value):
        self.set(key, value)
        return self

    # when set ,the object should be locked
    def set(self, key, value):
        if key is None:
            return False
        if value is None:
            return False
        # if key is None | value is None:
        #   return  False
        lock = Lock()
        lock.acquire()
        try:
            old_index = self.find_index_by_key(key)
            if old_index > -1:
                # there is a the same key in this dictionary, and replace it
                self.store[old_index] = value
                # update the seq of key-value insert
                self.delete_que_by_key(key)
                self.top += 1
                self.que[self.top] = key
                return True
            if self.top + 1 >= self.size:
                # table is full
                return False
            index = self.compute_index(key)
            if self.keys[index] is None:
                self.keys[index] = key
                self.store[index] = value
                self.top += 1
                self.que[self.top] = key
                return True
            else:
                index += 1
                while index < len(self.keys):
                    if self.keys[index] is None:
                        break
                    index += 1
                if index < len(self.keys):
                    self.keys[index] = key
                    self.store[index] = value
                    self.top += 1
                    self.que[self.top] = key
                    return True
        finally:
            lock.release()

    def get(self, key):
        if key is None:
            return False
        index = self.find_index_by_key(key)
        if index > -1:
            return self.store[index]
        else:
            return None

    def print(self):
        for i in self.que:
            print(str(i) + ":" + str(self.get(i)))

    def remove_by_key(self, key):
        if key is None:
            return False
        index = self.find_index_by_key(key)
        if index > -1:
            self.keys[index] = None
            ret = self.store[index]
            self.store[index] = None
            self.delete_que_by_key(key)
            return ret
        else:
            return False

    def remove_by_seq(self, seq):
        if seq >= self.size:
            return False
        if self.que[seq] is None:
            return False
        return self.remove_by_key(self.que[seq])

    def remove_by_value(self, value):
        for i in range(len(self.store)):
            if self.store[i] == value:
                return self.remove_by_key(self.keys[i])
        return False

    def get_size(self):
        return self.size

    def contains_value(self, item):
        for i in self.store:
            if i == item:
                return True
        return False

    def contains_key(self, item):
        for i in self.keys:
            if i == item:
                return True
        return False

    def mutFilter_key(self, p):
        for i in range(len(self.que)):
            if self.que[i] is None:
                break
            if not p(self.que[i]):
                self.remove_by_key(self.que[i])
                self.mutFilter_key(p)

    def map_value(self, p):
        for i in range(len(self.store)):
            if self.store[i] is not None:
                self.store[i] = p(self.store[i])

    def reduce_value(self, p):
        ret = 0
        for i in range(len(self.store)):
            if self.store[i] is not None:
                ret = p(ret, self.store[i])
        return ret

    def iter_key(self):
        self.a = 0
        return self

    def __iter__(self):
        self.a = 0
        return MyIter(self)

    def __next__(self):
        x = self.a
        self.a += 1
        if self.size <= x:
            raise StopIteration
        if self.que[x] is None:
            return None
        entry = MyEntry(self.que[x], self.get(self.que[x]))
        return entry

    def next_key(self):
        x = self.a
        self.a += 1
        if self.que[x] is None:
            return None
        return self.que[x]
