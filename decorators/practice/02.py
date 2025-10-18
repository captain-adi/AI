# print the function name and the values of its arguments every time the function called 

def logger(fn):
    def wrapper(*args,**kwargs):
        print(f"function name is :" , fn.__name__)
        print(", ".join(arg for arg in args))
        print( f"and all key arg is " , kwargs)
        fn(*args,**kwargs)
    return wrapper

@logger
def func(*args , **kwargs):
    print("hello")

func("hello" ,"aditya" , name="aditya pandey" ,  )