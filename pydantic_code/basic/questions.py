
from pydantic import BaseModel ,Field
from typing import Optional , List , Dict
# class User(BaseModel):
#     name : str
#     id : int
#     in_stock : bool
#     price : int = 0

# try:
#     product1 = User(id=1 , name="mixer"  )
# except Exception as e:
#     print(e)    




# questions number 2 : Create a Product model with name, price, and in_stock (default True).
# class Product(BaseModel):
#     name : str
#     price : float
#     in_stock : bool = True

# data = {"name": "Laptop", "price": 999.99}
# product1 = Product(**data)
# print(product1)


# 03 Create a Student model with name, roll_no, and optional email.

# class Student(BaseModel):
#     name :str
#     roll_no : int
#     email : Optional[str] = None

# student1 = Student(name="sunil" , roll_no=12 )
# print(student1)



# 04 : Create a Car model with model: str and year: int.
# class Car(BaseModel):
#     model:str
#     year : int

# car1 = Car(model="Tata" , year="1996")
# print(car1)



# 05 : Create a Post model that has a tags field (a list of strings).
# class Post(BaseModel):
#     tags  : List[str]

# post1 = Post(tags=["tag1", "tag2"])
# print(post1)


# 06 Create a Person model with age: int.
# Add a validator that raises an error if age < 18.

# class Person(BaseModel):
#     age : int = Field(..., ge=18)

# p1 = Person(age=16)