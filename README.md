
# _Report_

## Introduction

---

**Group name** _HDU_

**Group number** _LiXiao、LiChangMinChen_

**Laboratory work number**_1_

**Variant 8** _Dictionary based on hash-map, open address_

---

### Description of Lab *1*

Objectives:

- Use development tools:
  - Python 3, IDE/source code editor
  - git, Github Actions
  - laboratory work process
- Design **algorithms and data structures** in **mutable** styles
- Develop **unit and property-based tests**

### Variant *8*

1. You can use the built-in list for storing data.
2. You need to check that your implementation correctly works with None value
3. You need to implement functions/methods for getting/setting value by key.

### Features of the data structure implementation

- **Add** a new element `lst.add(3)`
- **Set** an element with specific index/key `lst.set(1,3)` if applicable
- **Remove** an element by `lst.remove(3)`
  - index for lists
  - key for dictionaries
  - value for sets value
- **Access**:
  - size `lst.size()`
  - is member `lst.member(3)`
  - reverse `lst.reverse()` (if applicable)
- **Conversion** from/to built-in`list`:
  - from_list`lst.from_list([12,99,37])`
  - to_list`lst.to_list()`
- **Filter** data structure by specific predicate `lst.filter(is_even)`
- **Reduce** process structure elements to build a return value by specific functions`lst.reduce(sum)`
- Data structure should be **an iterator** in Python style
- Data structure should be **a monoid** and implement `empty` and `concat` methods:
<!--
Suppose that `S` is a `set`, and • is some binary operation `S×S→S`
then`S` with • `(concat)` is a monoid if it satisfies the following two axioms:
- Associativity:
  For all `a,b` and `c` in `S`, the equation `(a•b)•c=a•(b•c)`holds.
- Identity element:
  There exists an element `e(empty)` in `S` such that,
  for every element `a` in `S`the equations`e•a=a•e=a` hold.
-->

<!--
__Pay extra attention to return values and corner cases like:__
1. What should happen, if a user puts **None** value to the data structure?
2. What should happen, if a user puts elements with **different types**
(e.g., *strings* and *numbers*)?
-->
