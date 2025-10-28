def process_order(item,quantity):
    print("item", item ,"Quantity" , quantity )
    try:
        if isinstance(quantity,int):
            prise = {"masala" : 20}[item]
            cost = prise * quantity
            print(f"You Should pay {cost}")
        else:
            raise ValueError("Quanity must be number")
    except KeyError:
        print("Sorry that is not availble in Store")
    except ValueError as e:
        print(f"Error : ", e)

process_order(item="ginger", quantity=2)
process_order(item="masala", quantity=4)