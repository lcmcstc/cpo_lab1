import unittest

from hypothesis import given
import hypothesis.strategies as st

from Hashmap_mutable import *

def test_hashmap(name):
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
    unittest.main()