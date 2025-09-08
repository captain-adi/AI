name = ['aditya','sumit','naresh']


#append  
name.append("ravi")
print(f"the list of name is : {name}" )

#remove
name.remove("aditya")
print(f"the list of name is : {name}" )


#count
print(f"the list of name is : {name.count("sumit")}" )


#extend
surnames = ["pandey","sahu","chamar"]

name.extend(surnames)
print(f"the list of name  and surname is : {name}" )


#insert in a perticular position 
name.insert(0,"aditya")
print(f"the new list after adding name is : {name}" )


#remove from perticular position :
last_name = name.pop()
print(f"Remove name from the last index : {name}" )


#reverse
name.reverse()
print(f"reverse name list is : {name}")


#sorting
name.sort()
print(f"sorted name list is : {name}")


age = ['23','21','22','24']
print(f"the age list is : {age}")

#max age
print(f"the max age is : {max(age)}")

#min age
print(f"the min age is : {min(age)}")