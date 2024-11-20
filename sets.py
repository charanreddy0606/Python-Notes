'''
Sets:it is an unordered collection of unique elements.
    sets are mutable,meaning you can add,delete elements after creation, but they do not allow duplicates.

'''
set1={1,2,3,4,5}
print(set1)
print(type(set1))

set1.add(3)
set1.add(99)
print(set1)

set1.remove(3)
print(set1)

set2={2,7,9,8,10}
print(set1 | set2)
print(set1 & set2)
print(set1 - set2)
