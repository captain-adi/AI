class Person:
    age = 21 

p1 = Person()
print(p1.age)
print(Person.age)
p1.age = 44

print(p1.age)
print(Person.age)

del p1.age
print(p1.age)