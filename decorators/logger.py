from functools import wraps
def log_activity(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        print("before")
        fn(*args,**kwargs)
        print("after")
    return wrapper

@log_activity
def say_hell(name,age):
    print(f"my name is {name} and my age is {age}")

say_hell("aditya",23)