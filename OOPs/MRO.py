class A:
    label = "Class A"

class B(A):
    label = "Class B"

class C(A):
    label =  "Class C"

class D(C,B):
    label = "Clss D"

test = D()
print(test.label)
print(D.__mro__)