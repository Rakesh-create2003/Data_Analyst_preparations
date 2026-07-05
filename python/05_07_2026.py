# Set in python:
# A set is an unordered collection of unique items.

# Key Characteristics
# Uses curly braces: {} or set()
# Unordered: no index positions
# Unique values only: duplicates are removed
# Mutable: you can add or remove items
# Good for membership tests and removing duplicates

# print(dir(set))
#  'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 
# 'intersection_update', 'isdisjoint', 'issubset', 'issuperset',
# 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'

# print(dir(dict))
# 'clear', 'copy', 'fromkeys', 'get','items', 'keys', 'pop', 
# 'popitem', 'setdefault', 'update', 'values']

# print(dir(tuple))
# 'count', 'index'

# print(dir(list))
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 
# 'remove', 'reverse', 'sort'

# Examples:
# 1.creating a set:
# fruits={"apple","banana","cherry"}
# print(fruits)
# print(type(fruits))

# 2. Accessing elements
# fruits={"apple","banana","cherry"}
# print(fruits)
# print(fruits[0])  # TypeError: 'set' object is not subscriptable

# 3. Modifying elements
# fruits={"apple","banana","cherry"}
# fruits[0]="kiwi"  # TypeError: 'set' object does not support item assignment

# 4.duplicate values are removed
# numbers={1,2,3,4,5,1,2,3}
# print(numbers)
# print(type(numbers))

# for num in numbers:
#     print(num)

# 5. add
# numbers={1,2,3,4,5}
# numbers.add(6)
# print(numbers)

# # # 6. remove
# numbers.remove(6)
# print(numbers)

# # 7. clear
# numbers.clear()
# print(numbers)

# # 8. pop
# values={1,2,3,4,5}
# values.pop()  
# print(values)
#
# Membership test
# items = {1,2,3,4,5}
# print(2 in items)
# print(6 in items)
# print(5 not in items)
# print(8 not in items)

# Set Operations
# a={1,2,3,4,5}
# b={4,5,6,7,8}
# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))
# print(b.difference(a))
# print(a.issubset(b))
# print(b.issubset(a))
# print(a.isdisjoint(b))

# values= []
# print(values)
# print(type(values))

# b=()
# print(b)
# print(type(b))

# c={}
# print(c)
# print(type(c))  

# d=set()
# print(d)
# print(type(d))

# Frozenset in Python
# A frozenset is an immutable version of a set — you cannot add or remove items after creation.

# Key Characteristics
# Immutable: cannot be changed after creation
# Unique values only
# Unordered collection
# Can be used as dictionary keys
# Can be elements of a set (unlike regular sets)
# Examples
# # 1. Creating a frozenset

# fruits =(["apple", "banana", "cherry"])
# print(fruits)
# print(type(fruits))
# fruit=frozenset(fruits)
# print(fruit)
# print(type(fruit))

# 2. Frozenset removes duplicates
# numbers =frozenset([1,2,3,3,4,4,5,5])
# print(numbers)
# print(type(numbers))

# 3. Set operations (union, intersection, etc.)

# a=frozenset([1,2,3,4,5])
# b=frozenset([4,5,6,7,8])
# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))
# print(b.difference(a))
# print(a.issubset(b))
# print(b.issubset(a))
# print(a.isdisjoint(b))

# Range 
# Definition:

# range produces an immutable sequence of integers: range(start, stop, step).
# start (default 0) is inclusive, stop is exclusive, step (default 1) is the increment.
# It's memory-efficient (lazy) and commonly used in loops.

#list(r) print(range(5))
# print(type(range(5)))
# print(list(range(5)))
# print(list(range(2,5)))
# print(list(range(2,10,3)))

# # 1.Basic (0..4)
# r=range(5)
# print(r)
# print(type(r))
# print(list(r))

# 2.Start/stop
# r=range(2,5)
# print(r)
# print(type(r))
# print()

# 3.Start/stop/step

# r=range(1,10,2)
# print(r)
# print(type(r))
# print(list(r))

# 4.Negative step (count down)
# r=range(10,5,-1)
# print(r)
# print(type(r))
# print(list(r))

# 5.common uses 
# for i in range(5):
#     print(i)

# for i in range(2,10):
#     print(i)


# for num in range(10):
#     # print(num)
    
#     if num%2==0:
#         print(f"{num} is an even number")

#     else:
#         print(f"{num} is an odd number")






