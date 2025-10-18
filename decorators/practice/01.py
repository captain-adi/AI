import time 

def calTime(fn):
    def wrapper():
        start = time.time()
        fn()
        end = time.time()
        print(end-start)
    return wrapper
@calTime
def greet():
    print("my name is aditya pandey")
greet()