

################pure and impure function ##########################

# def cout(num):
#     return num*100

# count_number = 100
# def another_count():
#     global count_number
#     return 100 * count_number

# print(cout(2))
# print(another_count())



#impure function
num =  0 
def increment():
    global num
    num += 1
    return num

print(increment())
print(increment())