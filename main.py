# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import threading
from threading import Lock


class MyEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "{" + str(self.key) + ":" + str(self.value) + "}"


class MyDictionary:

    def __init__(self, size):
        self.size = size
        self.store = [i for i in range(2 * size)]
        self.keys = [i for i in range(2 * size)]
        # que is used to record the seq of inserts
        self.que = [i for i in range(size)]
        self.top = -1
        for i in range(size):
            self.que[i] = None
        for i in range(2 * size):
            self.store[i] = None
            self.keys[i] = None

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

    # model hash
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

    # when set ,the object should be locked
    def set(self, key, value):
        if key is None:
            return False
        if value is None:
            return False
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
                self.remove_by_key(self.keys[i])
        return True

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
        ret = None
        for i in range(len(self.store)):
            if self.store[i] is not None:
                if ret is None:
                    ret = self.store[i]
                else:
                    ret = p(ret, self.store[i])
        return ret

    def iter_key(self):
        self.a = 0
        return self

    def next_key(self):
        x = self.a
        self.a += 1
        if self.que[x] is None:
            return None
        return self.que[x]


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print("init,size is three ,add (1, 23),(4, 66),(7, 98),(1, 78),(3, 48)")
    my_dictionary = MyDictionary(3)
    my_dictionary.set(1, 23)
    my_dictionary.set(4, 66)
    my_dictionary.set(7, 98)
    my_dictionary.set(1, 78)
    my_dictionary.set(3, 48)
    my_dictionary.print()
    print("--------------------------")
    print("remove key '7'  and  remove the one which is second inserted ")
    my_dictionary.remove_by_key(7)
    my_dictionary.remove_by_seq(1)
    my_dictionary.print()
    print("--------------------------")
    print("call tolist")
    print(my_dictionary.to_list())
    print("--------------------------")
    print("init a list,size is 2 [{lcmc:tc},{7758:5.61}],and then call form_list")
    tlist = [i for i in range(2)]
    tlist[0] = MyEntry("lcmc", "tc")
    tlist[1] = MyEntry(7758, 5.61)
    my_dictionary.from_list(tlist)
    my_dictionary.print()
    print("--------------------------")
    print("call mutFilter_key,remove the keys which are not typeof(int)")
    my_dictionary.mutFilter_key(lambda e: isinstance(e, int))
    my_dictionary.print()
    print("--------------------------")
    print("add {lcmc,66} into dictionary and call map_value , let every value add 1")
    my_dictionary.add("lcmc", 66)
    my_dictionary.map_value(lambda e: e + 1)
    my_dictionary.print()
    # if types of the values are different , there may be some error
    print("--------------------------")
    print("call reduce,sum all values , and if types of the values are different , there may be some error")
    print("sum:" + str(my_dictionary.reduce_value(lambda x, y: x + y)))
    print("--------------------------")
    print("use iter out two keys")
    my_dictionary = my_dictionary.iter_key()
    print(my_dictionary.next_key())
    print(my_dictionary.next_key())
    print("---------------")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('lcmc')
