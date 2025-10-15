# ✅ Create a list of numbers from 1 to 10 using list comprehension.
# lst = [i for i in range(1,11)]
# print(lst)


# ✅ Create a list of squares for numbers from 1 to 10.
# lst = [i**2 for i in range(1,11)]
# print(lst)


# ✅ Create a list of even numbers between 1 and 20.
# lst = [i for i in range(1,21) if i%2==0]
# print(lst)


# ✅ Create a list of odd numbers between 1 and 20.
# lst = [i for i in range(1,21) if i%2!=0]
# print(lst)

# ✅ Convert all strings in a list to uppercase.
# words = ["python", "is", "fun"]
# upperCaseWords = [i.upper() for i in words]
# print(upperCaseWords)


# ✅ Extract numbers greater than 50 from this list:
# nums = [10, 60, 23, 89, 100, 12]
# newList = [i for i in nums if i > 50]
# print(newList)


# ✅ From a list of words, extract only those that start with the letter 'A'.
# words = ["python", "is", "fun" , "aditya" , "Amit"]
# newList = [i for i in words if i.startswith("a" or "A")]
# print(newList)


# 🧠 Create a list of strings like "1-even", "2-odd", "3-even" … for numbers 1–10.
# newList = [f"{i}-even" if i%2==0 else f"{i}-odd" for i in range(1,11)]
# print(newList)

# 💡 Extract all numbers from a mixed list:
# data = [1, 'Aditya', 3.5, True, 10, 'Python']
# allNumbers = [i for i in data if type(i) is int ]
# print(allNumbers)


# 💡 Create a list of words with even length from a sentence:
# text = "Learning Python list comprehension is fun"
# newTextList = text.split(" ")
# newList = [(len(i),i) for i in newTextList ]
# print(newList)
