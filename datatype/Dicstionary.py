tea = {
     'name': 'Tea',
    'type': 'Beverage',
    'caffeine_content': 'Low'
}
print(tea)  # Output: {'name': 'Tea', 'type': 'Beverage', 'caffeine_content': 'Low'}



tea2 = dict(name="aditya",size="large",price=20)
print(tea2)  # Output: {'name': 'aditya', 'size': 'large', 'price': 20}



tea2["base"] = "milk"       # Adding a new key-value pair
tea2["price"] = 25          # Updating the value of an existing key
print(tea2)  # Output: {'name': 'aditya', 'size': 'large', 'base': 'milk', 'price': 25}


del tea2["size"]          # Deleting a key-value pair
print(tea2)  # Output: {'name': 'aditya', 'base':'milk', 'price': 25}


print(tea.values())


# lastItem = tea.popitem()
# print(f"the last item is : {lastItem}")
# print(tea)  # Output: {'name': 'Tea', 'type': 'Beverage'}

extraValues = {'sugar': 'yes', 'temperature': 'hot'}
tea.update(extraValues)  # Merging another dictionary
print(tea)  # Output: {'name': 'Tea', 'type': 'B