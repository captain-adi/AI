name1 = {'aditya','sumit','rahul'}
name2 = {'naresh','sumit','ravi'}
name_with_surname = name1 | name2

#union
print(f"the union of name and surname is : {name_with_surname}")


#common elements
print(f"the intersection of name1 and name2 is : {name1 & name2}")

#elements in name1 but not in name2
print(f"difference of name1 and name2 is : {name1 - name2}")



print(f"is aditya present in name1 : {'aditya' in name1}")




set = {'apple','banana','cherry',True,False,1}
print(set)