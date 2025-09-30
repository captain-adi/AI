def call_me(name):
    names = ["aditya","sumit","naresh"]
    if name not in names:
        raise ValueError("Plaze call me by my name ")

call_me("dj")