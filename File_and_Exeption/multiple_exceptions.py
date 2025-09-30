def process(item,quan):
    try:
        price = {"masala" :  20}[item]
        cost = price * quan
        print(f"total const {cost}")
    except KeyError:
        print("sorry we do not have that chai")
    except TypeError:
        print("quantity must be number")

process("ginger",2)
process("masala","two")