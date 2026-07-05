#What is python in Interview Points?
#Python is a high-level, interpreted programming language known for its simplicity
# and readability.

#Who is using Python?
#Python is used by developers, researchers, scientists, and data analysts 
#for a wide range of applications, including web development, 
#data analysis, machine learning, and more.

#Why use Python?
# Used for scripting, web development, data analysis, automation, AI/ML
#Python is a versatile language that can be used for a wide range of applications,
#including web development, data analysis, machine learning, and more.

# Who is introducing Python?
# #Python was introduced by Guido van Rossum in 1991.

# Python Data Types — Definitions and Examples (primitives Data types)

# 1.int (Integer)
# Definition: Whole numbers without a decimal point.
# Use: counting, indexing, arithmetic.
# Examples:

# x = 10
# print(x)
# print(type(x))
# y = -5
# print(y)
# print(type(y))

# z = 0
# print(z)
# print(type(z))

# total = 2 + 3
# print(total)
# print(type(total))

# power = 4 ** 3 # 64
# print(power)
# print(type(power))

# 2. float (Floating-Point)
# Definition: Numbers with a decimal point or exponent notation.
# Use: measurements, division, scientific values.
# Examples:

# pi = 3.14
# rate = 0.25
# value = 1.0
# result = 5 / 2 # 2.5
# scientific = 1.2e3 # 1200.0
# print(pi)
# print(type(pi))
# print(rate)
# print(type(rate))
# print(value)
# print(type(value))
# print(result)
# print(type(result))
# print(scientific)
# print(type(scientific))

# 3. complex
# Definition: Numbers with real and imaginary parts, written a + bj.
# Use: electrical engineering, signal processing, math.
# Examples:

# c1 = 2 + 3j
# c2 = complex(4, -1)
# real_part = c1.real # 2.0
# imag_part = c1.imag # 3.0
# sum = c1 + c2
# print(sum)
# print(type(sum))

# 4. bool (Boolean)
# Definition: Logical values True or False.
# Use: conditions, comparisons, flags.
# Examples:

# is_valid = True
# has_access = False
# check = 5 > 3 # True

# print(is_valid)
# print(type(is_valid))
# print(has_access)
# print(type(has_access))
# print(check)
# print(type(check))

# 5. str (String)
# Definition: Text enclosed in single or double quotes.
# Use: text, file paths, user input.
# Examples:

# name = "John"
# message = 'Hello, world!'
# print(name)
# print(type(name))
# print(message)
# print(type(message))

# 6.Nonetype
# Definition: Represents the absence of a value or a null value.
# Use: variables that have not been assigned a value yet.
# Examples:

# x = None
# print(x)
# print(type(x))

# Non-primitive Data types in Python

# List in Python
# A list is a built-in data type used to store multiple items in a single variable.

# Definition
# A list is an ordered, changeable, and indexed collection of items.
# It allows duplicate values.
# It is written with square brackets [].

# Examples
# 1. Creating a list
# fruits = ["apple", "banana", "cherry"]
# print(fruits)
# print(type(fruits))

# 2. Accessing elements
# fruits = ["apple", "banana", "cherry"]
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])

# 3. Modifying elements
# fruits = ["apple", "banana", "cherry"]
# fruits[0] = "kiwi"
# print(fruits)

# 4. Adding elements
# fruits = ["apple", "banana", "cherry"]
# fruits.append(["orange"])
# print(fruits)

# 5. Removing elements
# fruits = ["apple", "banana", "cherry"]
# fruits.remove("banana")
# print(fruits)

# 6. Slicing lists
# fruits = ["apple", "banana", "cherry", "kiwi", "orange"]
# print(fruits[1:3])
# print(fruits[:3])
# print(fruits[2:])

# 7. Sorting lists
# fruits = ["apple", "banana", "cherry", "mango", "kiwi", "orange"]
# fruits.sort()
# print(fruits)

# print(dir(list)) # Built-in methods of list
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'.

# 8. List Comprehension
# List comprehension is a concise way to create lists in Python.
# It allows you to create a new list by applying a function to each element of an existing list.

# Syntax    
# new_list = [expression for item in iterable if condition]

# Example
# numbers = [1, 2, 3, 4, 5]
# even_numbers = [num for num in numbers if num % 2 == 0]
# print(even_numbers)

# numbers = [1, 2, 3, 4, 5]
# value=numbers.remove(3)
# print(value)
# print(numbers)  

# numbers = [1, 2, 3, 4, 5]
# value=numbers.pop(3)
# print(value)
# print(numbers)  

# 9. List with Mixed Data Types
# A list can contain elements of different data types, such as integers, strings, and floats.
# Example

# mixed_list = [1, "apple", 3.14, "banana", 5]
# print(mixed_list)
# print(type(mixed_list))

# Tuple in Python
# A tuple is an ordered collection of items that is immutable (cannot be changed after creation).

# Key points
# Written with parentheses: ()
# Ordered: keeps insertion order
# Immutable: you cannot add, remove, or modify items
# Can contain different data types
# Allows duplicates

# Example
# fruits = ("apple", "banana", "cherry", "apple")
# print(fruits)
# print(type(fruits))

# create a tuple
# point = (10, 20)
# print(point)  
# print(type(point))
# print(point[1])  # Accessing elements
# print(2*point)
# print(point)

# 2. Tuple with Mixed Data Types
# A tuple can contain elements of different data types, such as integers, strings, and floats.
# Example
# mixed_values =(1,"Rakesh",8.2,"3j+1",["anura",22,True])
# print(mixed_values)
# print(type(mixed_values))
# print(mixed_values[3])  # Accessing elements
# print(mixed_values[4][1])  # Accessing elements in the list inside the tuple

#3. unpack tuple into variables
# num,name,float,complex,list = mixed_values
# print(num)
# print(name)
# print(float)
# print(complex)
# print(list)

# Dictionary in Python
# A dictionary is an unordered collection of key-value pairs,
# used to store data where each key is unique and maps to a value.

# Key points
# Written with curly brackets: {}
# Unordered: keys are not in any particular order
# Mutable: you can add, remove, or modify keys and values
# Can contain different data types
# Allows duplicates

# Example
# 1. creating a dictionary
# person = {"name":"Rakesh","age":22,"city":"chennai","marks":[85, 90, 78]}
# print(person)
# print(type(person))

# 2. Accessing values
# print(person["name"])  # Accessing value by key
# print(person.get("age"))  # Accessing value using get() method
# print(person.keys())  # Accessing keys
# print(person.values())  # Accessing values
# print(person.items())  # Accessing key-value pairs
# print(person["marks"][1])  # Accessing value in the list inside the dictionary
# print(person.get(22))
# print(len(person))  # Getting the number of key-value pairs in the dictionary

# 3. Adding new key-value pairs
# person["country"]="India"
# print(person)

# person.update({"email":"sIb0j@example.com"})
# print(person)

# person["mobile"]="1234567890"
# print(person)

# print(person.keys())
# print(person.values())
# print(person.items())

# 4. Modifying values
# person["name"]="Rakeshwar"
# print(person)

# print(person["name"])  # Accessing value by key 

# 5. Removing key-value pairs
# print(person.pop("age"))  # Removing a key-value pair by key
# print(person)

# del person["city"]  # Removing a key-value pair by key
# print(person)
# print(person.pop("marks"))  # Removing a key-value pair by key

# 6. Checking if a key exists
# print("name" in person)  # Checking if a key exists in the dictionary
# print("name" not in person)  # Checking if a key does not exist in the dictionary

#7.Dictionary with Mixed data Types
# A dictionary can contain elements of different data types, such as
#  integers, strings, lists, and tuples.

# students={
#     "name":"Rakesh",
#     "age":22,
#     "marks":[85, 90, 78],
# }    
# print(students)
# print(type(students))

# print(students.keys())  # Accessing keys
# print(students.values())  # Accessing values
# print(students.items())  # Accessing key-value pairs

#8. Iterating through a dictionary
# person = {
#     "name":"Rakesh",
#     "age":22,
#     "marks":[85,90,78],
#     }
# for key in person:
#     print(key,":",person[key])  # Accessing key-value pairs
    
# problem solving Questions
# numbers=[1,2,3,4,5,6,7,8,9,10]

# for num in numbers:
#     if num%2==0:
#         print(num,"is even")
#     else:
#         print(num,"is odd")

# 9. Checking if key exists
# person={
#     "name":"Rakesh",
#     "age":22,
#     "marks":[85,90,78],

# }
# if "name" in person:
#     print("Name exists in the dictionary")
# else:
#     print("Name is not found in the dictionary")

# 10. Using get() method

person={
    
    "name":"Rakesh",
    "age":22,
    "marks":[85,90,78],
    "city":"chennai"
}
# print(person)
# print(type(person))
# print(person.get("name"))  # Accessing value using get() method
# print(len(person))  # Getting the number of key-value pairs in the dictionary
# del person["city"]
# print(person)

# Looping Through and Getting Values
# for values in person:
#     # print(values)  # Accessing key-value pairs   
#     # print(person[values])  # Accessing value by key
#     print(values,":",person[values])  # Accessing key-value pairs




