name = ["aditya","sumit"]
print(name[1])

try:
    print(name["sumit"])
except TypeError:
    print("the type error ")