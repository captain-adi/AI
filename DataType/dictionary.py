user = {
    "name" : "aditya" ,
    "age" : 24 ,
    "city" : "bangalore" ,
    "address" : {
        "street" : "xyz" ,
        "pincode" : 560037
    }
}


# del item 
del user["address"]

#add new property 
user["phoneNumber"] = "1234243243"


user.pop("age")
print(user)

#loop

for i in user.values():
    print(i )

print(len(user))
