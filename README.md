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

---

### Variant *8*

- You can use the built-in list for storing data.
- You need to check that your implementation correctly works with None value.
- You need to implement functions/methods for getting/setting value by key.

---

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

> Suppose that `S` is a `set`, and • is some binary operation `S×S→S`
> then`S` with • `(concat)` is a monoid if it satisfies the following two axioms:
> Associativity:
> For all `a,b` and `c` in `S`, the equation `(a•b)•c=a•(b•c)`holds.
> Identity element:
> There exists an element `e(empty)` in `S` such that,
> for every element `a` in `S`the equations`e•a=a•e=a` hold.

- __Pay extra attention to return values and corner cases like:__

  - What should happen, if a user puts **None** value to the data structure?
  - What should happen, if a user puts elements with **different types**?

---

### Code

- Add

    ```
    def add(self, key, value):
        self.set(key, value)
        return self
    ```

- Set

    ```
    from threading import Lock
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
    ```

- Remove

   - index for lists
      ```
      def remove_by_seq(self, seq):
          if seq >= self.size:
              return False
          if self.que[seq] is None:
              return False
          return self.remove_by_key(self.que[seq])
      ```
   - key for dictionaries
      ```
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
      ```
   - value for sets value
      ```
      def remove_by_value(self, value):
          for i in range(len(self.store)):
              if self.store[i] == value:
                  return self.remove_by_key(self.keys[i])
          return False
      ```

- Access

  - size
     ```
     def get_size(self):
         return self.size
     ```
  - is member
     ```
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
     ```
  - reverse(if applicable)

- Conversion

    ```
    from Hashmap_mutable import MyEntry
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
    ```

- Filter

    ```
    def mutFilter_key(self, p):
        for i in range(len(self.que)):
            if self.que[i] is None:
                break
            if not p(self.que[i]):
                self.remove_by_key(self.que[i])
                self.mutFilter_key(p)
    ```

- Map

    ```
    def map_value(self, p):
        for i in range(len(self.store)):
            if self.store[i] is not None:
                self.store[i] = p(self.store[i])
    ```

- Reduce

    ```
    def reduce_value(self, p):
        ret = 0
        for i in range(len(self.store)):
            if self.store[i] is not None:
                ret = p(ret, self.store[i])
        return ret
    ```

- iter

    ```
    from Hashmap_mutable import MyEntry
    def __iter__(self):
        self.a = 0
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        if self.size <= x:
            raise StopIteration
        if self.que[x] is None:
            return None
        entry = MyEntry(self.que[x], self.get(self.que[x]))
        return entry
    ```

---