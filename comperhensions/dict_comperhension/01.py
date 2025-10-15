


# From numbers 1–10, create a dictionary containing only even numbers as keys and their square as values.
# squares_dict = {i:i**2 for i in range(1,6) if i%2==0}
# print(squares_dict)



# 2. Create a dictionary from this list of numbers [1,2,3,4] where each number is the key and its double is the value.

# lst =[1,2,3,4]
# newDict = {i:i*2 for i in lst}
# print(newDict)


# 3 . Convert this list to a dictionary where the word is the key and its length is the value:
# words = ["Python", "Java", "C++"]
# newDict = {i:len(i) for i in words}
# print(newDict)


# Create a dictionary from two lists:
# names = ["Aditya", "Ravi", "Neha"]
# marks = [85, 60, 95]
# newDist = {i:x for i in names for x in marks }
# print(newDist)


# Create a dictionary from a string containing counts of each character:
# text = "python"
# newDist = {x:len(x) for x in text}
# print(newDist)

# Create a dictionary where keys = numbers 1–10, values = factorial of the key (use import math).

# import math

# newDist = {x:math.factorial(x) for x in range(1,11)}
# print(newDist)



# From two lists, create a dictionary, but skip items where the mark is < 50:
names = ["Aditya", "Ravi", "Neha"]
marks = [85, 40, 95]
newDist = {name:mark if mark> 50 else "fail" for name, mark in zip(names,marks)}
print(newDist)