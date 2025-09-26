class Name():
    def __init__(self , firstName , lastName ):
        self.firstName = firstName
        self.lastName = lastName

    def generateName(self):
        return f"my First name is {self.firstName} And Last Name is {self.lastName}"

name = Name("aditya","pandey")
print(name.generateName())
name1 = Name("adarsh","pandey")
print(name1.generateName())