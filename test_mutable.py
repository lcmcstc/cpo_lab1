import unittest
from hypothesis import given
import hypothesis.strategies as st
from Hashmap_mutable import *


class TestDict(unittest.TestCase):
    def test_size(self):
        self.assertEqual(MyDictionary(3).dic_size, 3)
        self.assertEqual(MyDictionary(0).dic_size, 0)

    def test_add(self):
        test_dict = MyDictionary(2)
        test_dict.set(0, 0)
        test_dict.set(1, 1)
        dic={0:0,1:1}
        mydict=MyDictionary()
        mydict.from_list(dic)
        self.assertEqual(mydict, test_dict)


    def test_set(self):
        test_dict = MyDictionary(5)
        test_dict.set(9, 3)
        test_dict.set(0, 0)
        test_dict.set(1, 1)
        test_dict.set(2, 2)
        mydict = MyDictionary(5)
        mydict.set(9, 3)
        for i in range(3):
            mydict.set(i, i)
        self.assertEqual(mydict, test_dict)

    def test_remove(self):
        test_dict = MyDictionary(5)
        test_dict.set(0, 0)
        test_dict.set(4, 2)
        test_dict.set(6, 3)
        test_dict.set(8, 4)
        mydict = MyDictionary(5)
        for i in range(5):
            mydict.set(2 * i, i)
        mydict.remove(2)
        self.assertEqual(mydict, test_dict)

    def test_access(self):
        mydict = MyDictionary(5)
        for i in range(5):
            mydict.set(2 * i, i)
        dic = {}
        for i in range(5):
            dic[2 * i] = i
        for item in dic.items():
            self.assertTrue(mydict.__contains__(item))

    def test_to_list(self):
        self.assertDictEqual(MyDictionary().to_list(), {})

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
        mydict.map(str)
        self.assertEqual(mydict.to_list(), {})
        mydict = MyDictionary(3)
        tlist = {11: 1, 22: 2, 33: 3}
        mydict.from_list(tlist)
        tolist_1 = mydict.to_list()
        self.assertEqual(tolist_1, tlist)
        mydict.map(lambda x: x + 1)
        tolist_2 = mydict.to_list()
        tlist3 = {}
        for item in tlist.items():
            tlist3[item[0]] = item[1] + 1
        self.assertEqual(tolist_2, tlist3)

    def test_reduce(self):
        myd = MyDictionary()
        str(myd.reduce(lambda x, y: x + y))
        self.assertEqual((myd.reduce(lambda x, y: x + y)), 0)
        myd = MyDictionary()
        tlist = {1: 1, 2: 2, 3: 3}
        myd.from_list(tlist)
        self.assertEqual(myd.reduce(lambda x, y: x + y), 6)
        test_data = {1: 'a', 2: 'b', 3: 'c'}
        myd = MyDictionary(3)
        myd.from_list(test_data)
        myd.print()
        myd1 = MyDictionary(3)
        myd1.from_list(tlist)
        self.assertEqual(myd1.reduce(lambda x, _: x + 1), myd1.dic_size)

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
        self.assertEqual(myd.dic_size, len(a))

    def test_iter(self):
        tlist = {1: 1, 2: 2, 3: 3}
        myd = MyDictionary()
        myd.from_list(tlist)
        tmp = {}
        for e in myd:
            tmp[e[0]] = e[1]
        self.assertEqual(tlist, tmp)
        self.assertEqual(myd.to_list(), tmp)

    def test_reverse(self):
        tlist = MyDictionary()
        self.assertEqual(tlist, tlist.empty())

    def test_empty(self):
        dic = {0: 'a', 1: 'b', 3: 'c', 4: 'd'}
        test_dict = MyDictionary().from_list(dic)
        test_dict2 = MyDictionary().from_list(dic)
        test_dict.reverse()
        test_dict.print()
        test_dict2.print()
        test_dict.reverse()
        self.assertEqual(test_dict, test_dict2)

    def test_contact(self):
        test_dict = MyDictionary(2)
        test_dict.set(0, 'a')
        test_dict.set(1, 'b')
        test_dict2 = MyDictionary(2)
        test_dict2.set(3, 'c')
        test_dict2.set(4, 'd')
        test_dict3 = test_dict.contact(test_dict2)
        dic = {0: 'a', 1: 'b', 3: 'c', 4: 'd'}
        test_dict4 = test_dict.from_list(dic)
        self.assertEqual(test_dict3, test_dict4)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    unittest.main()
