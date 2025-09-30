class customExceptions(Exception):
    pass

def say_my_name(name):
    if name == "aditya":
        print(f"hello {name}")
    else:
        raise customExceptions("you are calling by wrong name")

say_my_name("sumit")