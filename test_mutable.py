import unittest
from hypothesis import given
import hypothesis.strategies as st
from Hashmap_mutable import *


class TestDict(unittest.TestCase):
    def test_size(self):
        print("start testing Dict.size")
        self.assertEqual(MyDictionary(3).size, 3)
        self.assertEqual(MyDictionary(0).size, 0)
        print("-----------over----------")

    def test_add(self):
        print("start testing Dict.add()")
        mydict = MyDictionary(5)
        for i in range(10):
            mydict.add(i, i)
        mydict.print()
        print("-----------over----------")

    def test_set(self):
        print("Start testing Set")
        mydict = MyDictionary(5)
        mydict.set(9, 3)
        for i in range(3):
            mydict.set(i, i)
        mydict.print()
        print("-----------over----------")

    def test_remove(self):
        print("Start testing Remove")
        mydict = MyDictionary(5)
        for i in range(5):
            mydict.set(2 * i, i)
        mydict.print()
        print("Dict.remove_by_seq(2),delete by index")
        print("Deleted value =", mydict.remove_by_seq(2))
        print("Dict.remove_by_key(2),delete by key")
        print("Deleted value =", mydict.remove_by_key(2))
        print("Dict.remove_by_value(3)，delete by value")
        print("Deleted value =", mydict.remove_by_value(3))
        mydict.print()
        print("-----------over----------")

    def test_access(self):
        print("start testing Dict.Access")
        mydict = MyDictionary(5)
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

    def test_to_list(self):
        self.assertEqual(MyDictionary().to_list(), {})

        test_list_1 = {0: 123}
        tlist = MyDictionary(1).add(0, 123).to_list()
        self.assertEqual(tlist, test_list_1)

        test_dict = MyDictionary(2)
        test_dict.set(0, 'a')
        test_dict.set(1, 'b')
        test_list_2 = {0: 'a', 1: 'b'}
        tlist = test_dict.to_list()
        self.assertEqual(tlist, test_list_2)

    def test_from_list(self):
        mydict = MyDictionary()
        mydict.from_list({})
        self.assertEqual(mydict.to_list(), {})
        test_list_1 = {"test": 1}
        mydict.from_list(test_list_1)
        tlist_1 = mydict.to_list()
        self.assertEqual(tlist_1, test_list_1)

        test_list_2 = {"test": 1, 7758: 5.61}
        mydict.from_list(test_list_2)
        tlist_2 = mydict.to_list()
        self.assertEqual(tlist_2, test_list_2)

    def test_map(self):
        mydict = MyDictionary()
        mydict.map_value(str)
        self.assertEqual(mydict.to_list(), [])

        mydict = MyDictionary(3)
        tlist = [i for i in range(3)]
        tlist[0] = MyEntry(11, 1)
        tlist[1] = MyEntry(22, 2)
        tlist[2] = MyEntry(33, 3)
        mydict.from_list(tlist)
        tolist_1 = mydict.to_list()
        tolist_1.__eq__(tlist)
        mydict.map_value(lambda x: x + 1)
        tolist_2 = mydict.to_list()
        tolist_2.__eq__(tlist)
        for i in range(3):
            tolist_2[i].__eq__(tlist[i])
            print(tolist_2[i])

    def test_reduce(self):
        myd = MyDictionary()
        str(myd.reduce_value(lambda x, y: x + y))
        self.assertEqual((myd.reduce_value(lambda x, y: x + y)), 0)
        myd = MyDictionary()
        tlist = [i for i in range(3)]
        tlist[0] = MyEntry(1, 1)
        tlist[1] = MyEntry(2, 2)
        tlist[2] = MyEntry(3, 3)
        myd.from_list(tlist)
        self.assertEqual(myd.reduce_value(lambda x, y: x + y), 6)
        test_data = [i for i in range(3)]
        test_data[0] = MyEntry(1, 'a')
        test_data[1] = MyEntry(2, 'b')
        test_data[2] = MyEntry(3, 'c')
        myd = MyDictionary(3)
        myd.from_list(test_data)
        myd.print()
        myd1 = MyDictionary(3)
        myd1.from_list(tlist)
        self.assertEqual(myd1.reduce_value(lambda x, _: x + 1), myd1.size)

    @given(st.dictionaries(st.integers(), st.integers()))
    def test_from_list_to_list_equality(self, a):
        myd = MyDictionary(len(a))
        myd.from_list(a)
        b = myd.to_list()
        self.assertEqual(a, b)

    @given(st.dictionaries(st.integers(), st.integers()))
    def test_python_len_and_list_size_equality(self, a):
        myd = MyDictionary(len(a))
        myd.from_list(a)
        self.assertEqual(myd.size, len(a))

    def test_iter(self):
        tlist = {1: 1, 2: 2, 3: 3}
        myd = MyDictionary()
        myd.from_list(tlist)
        tmp = {}
        for e in myd:
            tmp.append(e)
        self.assertEqual(tlist, tmp)
        self.assertEqual(myd.to_list(), tmp)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    unittest.main()
