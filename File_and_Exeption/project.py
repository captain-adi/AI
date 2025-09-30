class customException(Exception): pass


def give_order(flavor,cup):
    menu = {"masala":20,"ginger":40}
    try:
        if flavor not in menu:
            raise customException("we do not have that flavor")
        if not isinstance(cup,int):
            raise TypeError("type error of cup")
        total = menu[flavor] * cup
        print(f"finally u should pay : {total}")
    except Exception as e :
        print(e)
         
        
 

 
give_order("masala","two")
give_order("mint",2)
give_order("ginger",4)