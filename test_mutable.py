import unittest
from hypothesis import given
import hypothesis.strategies as st
from Hashmap_mutable import *
class TestDict(unittest.TestCase):
    def test_size(self):
        print("start testing Dict.size")
        self.assertEqual(MyDictionary(3).size,3)
        self.assertEqual(MyDictionary(0).size,0)
        print("-----------over----------")
    def test_add(self):
        print("start testing Dict.add()")
        mydict = MyDictionary(5);
        for i in range (10):
            mydict.add(i,i)
        mydict.print()
        print("-----------over----------")
    def test_set(self):
        print("Start testing Set")
        mydict = MyDictionary(5);
        mydict.set(9,3)
        for i in range(3):
            mydict.set(i,i)
        mydict.print()
        print("-----------over----------")
    def test_remove(self):
        print("Start testing Remove")
        mydict = MyDictionary(5);
        for i in range(5):
            mydict.set(2*i, i)
        mydict.print()
        print("Dict.remove_by_seq(2),delete by index")
        print("Deleted value =",mydict.remove_by_seq(2))
        print("Dict.remove_by_key(2),delete by key")
        print("Deleted value =",mydict.remove_by_key(2))
        print("Dict.remove_by_value(3)，delete by value")
        print("Deleted value =",mydict.remove_by_value(3))
        mydict.print()
        print("-----------over----------")
    def test_access(self):
        print("start testing Dict.Access")
        mydict = MyDictionary(5);
        for i in range(5):
            mydict.set(2 * i, i)
        mydict.print()
        print("Dict.size()")
        print(mydict.get_size())
        print("Dict.member()==contains_value(2)")
        print(mydict.contains_value(2))
        print("Dict.member()==contains_key(3)")
        print(mydict.contains_key(3))
        print("-----------over----------")
    def test_from_list(self):
        mydict = MyDictionary(5);
        for i in range(5):
            mydict.set(2 * i, i)
        print("to_list()")
        ret=mydict.to_list()
        for i in range(5):
            print(ret[i].key,ret[i].value)
        print("-----------over----------")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    unittest.main()