def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function runs")
        print(f"Arguments received: {args}, {kwargs}")

        result = func(*args, **kwargs)  # calling the original function

        print("After function runs")
        return result  # important to return result if the original function returns something
    return wrapper


@my_decorator
def add(*args):
    sum = 0
    for i in args:
        sum = sum + i  
    return sum


total = add(34,1,2,3)
print("Result:", total)
