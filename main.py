# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import threading
from threading import Lock


class MyDictionary:
    Node_value = "Nothing"

    def __init__(self, size):
        self.size = size
        self.store = [i for i in range(size)]
        self.keys = [i for i in range(size)]
        for i in range(size):
            self.store[i] = None
            self.keys[i] = None

    def compute_index(self, key):
        hash_value = hash(key)
        if hash_value < 0:
            hash_value = hash_value * -1
        return hash_value % self.size

    # when set ,the object should be locked
    def set(self, key, value):
        if key is None:
            self.Node_value = value
            return
        index = self.compute_index(key)
        lock = Lock()
        lock.acquire()
        try:
            if self.keys[index] is None:
                self.keys[index] = key
                self.store[index] = value
            else:
                index += 1
                while index < self.size:
                    if self.keys[index] is None:
                        break
                    index += 1
                if index < self.size:
                    self.keys[index] = key
                    self.store[index] = value
        finally:
            lock.release()

    def get(self, key):
        if key is None:
            return self.Node_value
        index = self.compute_index(key)
        if self.keys[index] == key:
            return self.store[index]
        else:
            index += 1
            while index < self.size:
                if self.keys[index] == key:
                    return self.store[index]
                if self.keys[index] is None:
                    return "Not Find"
                index += 1
            return "Not Find"


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    my_dictionary = MyDictionary(3)
    my_dictionary.set(None, 655)
    my_dictionary.set(1, 777)
    my_dictionary.set(3, 681)
    print(my_dictionary.get(None))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('lcmc')
