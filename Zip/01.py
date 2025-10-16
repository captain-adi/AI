marks = [21,23,12,43]
names = ["aditya", "sumit","ram" , "raju"]
# zipFormt = list(zip(names,marks))

# for name in zipFormt:
#     print(f"name is {name} ")




# ⚠️ Note

# Once you loop through a zip object once, it’s exhausted.
# So if you need to use it multiple times, convert it to a list first:

newZip = zip(names,marks)
for i in newZip:
    print(i)
for i in newZip:
    print(i)
