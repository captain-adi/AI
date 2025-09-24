from functools import wraps
def my_decorator(fn):
    @wraps(fn)
    def myWrapper():
        print("before")
        fn()
        print("after")
    return myWrapper

@my_decorator
def sayHello():
    print("my name is aditya Pandey")

sayHello()
print(sayHello.__name__)