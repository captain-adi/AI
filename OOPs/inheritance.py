class Person:
    def __init__(self, name , age):
        self.name = name
        self.age = age
    def generateName(self):
        return f"my name is : {self.name} and age is : {self.age} "
class Address(Person):
    def printAddressWithName(self):
        return f"my address is 2323"