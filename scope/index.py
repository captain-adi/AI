def outerfn(num):
    def innerfn(v):
        return v ** num
    return innerfn

result = outerfn(2)
print(result(2))