class Names():
    name = "aditya"
    def sayName(self):
        return f"my name is : {self.name}"


obj = Names()
obj1 = Names()
print(obj.sayName())
print(Names.sayName(obj))
obj1.name = "sumit"
print(Names.sayName(obj1))