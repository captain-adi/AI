# def admin_routes(fn):
#     admin = False
#     def wrapper():
#         if admin == True:
#             print("you can access the data")
#             fn()
#         else:
#             print("You are not admin and You can not access the data")
#     return wrapper

# @admin_routes
# def info():
#     print("the is the secrete password")
# info()



# def admin_routes(fn):
#     admin = True
#     def wrapper():
#         if admin==True:
#             fn()
#         else:
#             print("you are not admin")
#     return wrapper


# @admin_routes
# def info():
#     print("this is all Data")
 
# info()


def check_role(fn):
    def wrapper(role):
        if role == "Admin":
            print("You can access")
        else:
            print("you can not access ")
    return wrapper

@check_role
def access_admin_panel(role):
    print("Data")

access_admin_panel("Admin")
access_admin_panel("User")