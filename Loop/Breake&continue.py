orders  = ["chai","coffe","lemonSoda"]
inputValue = input("can i have your order plz..: ")

# Use enumerate to get both index and value from a list
for index, order in enumerate(orders,start=1):
    if order == inputValue:
        print(f"you order chai")
    if order == "nothing":
        break
    print("you order nothing ")
