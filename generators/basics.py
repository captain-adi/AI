def sayHello():
    yield "hello first time"
    yield "hello second time"
    yield "hello third time"

result = sayHello()
print(next(result))
print(next(result))