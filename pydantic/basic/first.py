from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    is_admin: bool = False  # default value

data = {"name":"aditya" , "age": "two" , "is_admin" : True }

userData = User(**data)
print(type(userData.age))