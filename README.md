# HDU - lab 1 - variant 8

## Variant 8

Dictionary based on hash-map, open address

## laboratory work description

• Add a new element  (lst.add(3))
• Set an element with specific index / key (lst.set(1, 3)) if applicable.
• Remove an element by (lst.remove(3)):

- index for lists
- key for dictionaries - value for sets value

• Access:

- size (lst.size())
- is member (lst.member(3))
- reverse (lst.reverse() (if applicable)

• Conversion from/to built-in list :

- from_list (lst.from_list([12, 99, 37]))
- to_list (lst.to_list())

• Filter data structure by specific predicate (lst.filter(is_even))
• Map1 structure by specific function (lst.map(increment))
• Reduce2 – process structure elements to build a return value by specific functions(lst.reduce(sum))
• Data structure should be an iterator3 in Python style
• Data structure should be a monoid and implement empty and concat methods

## Project structure

- `Hashmap_mutable.py` -- implementation of `Dictionary` class with `add` etc.
- `test_mutable.py` -- unit and PBT tests for `Dictionary`.

## Features

- `to_list( )`
- `from_list(tlist)`
- `compute_index(key)`
- `delete_que_by_key(key)`
- `find(key)`
- `add(key, value)`
- `set(key, value)`
- `get(key)`
- `remove(key)`
- `size( )`
- `_contains_(item)`
- `contains_value(item)`
- `contain_key(item)`
- `filter(p)`
- `map(p)`
- `reduce(p)`
- `empty( )`
- `concat(other)`
- `reverse()`
- `__next__( )`
- `__iter__( )`
- PBT: `test_from_list_to_list_equality(a)`
- PBT: `test_python_len_and_list_size_equality(a)`

## Contribution

- Li ChangMinChen (212320023@hdu.edu.cn) -- Hashmap_mutable.py
- Li Xiao (212320022@hdu.edu.cn) -- test_mutable.py and README.md

## Changelog

- 24.04.2022 - 48
  - Update README.md
- 24.04.2022 - 47
  - add .gitignore
- 24.04.2022 - 46
  - fix module naming and rewrite the `contains` function
- 24.04.2022 - 45
  - clean the repository from unnecessary artefacts, like `.hypothesis` work data
- 24.04.2022 - 44
  - add `reverse`、`empty`、`contact`
- 24.04.2022 - 43
  - fixed `__next__` feature
- 24.04.2022 - 42
  - model the dictionary instead of creating my own one
- 24.04.2022 - 41
  - fixed `the two iterators on one data structure work in parallel incorrectly`
- 22.04.2022 - 38-40
  - Update README.md and fix file format issues
- 21.04.2022 - 30-37
  - Update README.md with file format issues
- 19.04.2022 - 18-29
  - Update README.md with file format issues
- 18.04.2022 - 15-17
  - Complete test.py
- 14.04.2022 - 5-14
  - Create main.yml
- 13.04.2022 - 2-4
  - Add `test_mutable.py`, Create README.md
- 12.04.2022 - 1
  - Complete `Hashmap_mutable.py`
- 12.04.2022 - 0
  - Initial commit

## Design notes

- Create `Myentry` class to implement key-value pairs.
- Create `MyIter` class to implement `__iter__` and `__next__`.
- Create `MyDictionary` class to implement the dictionary.
