##Activity 6.Finding Items in Lists with the in Operator
# Sample list

my_list = [10, 20, 30, 40, 50]

# Check if an item is in the list using the 'in' operator
item_to_check = 30
if item_to_check in my_list:
    print(f"{item_to_check} is in the list.")
else:
    print(f"{item_to_check} is not in the list.")

# Check if an item is not in the list using the 'not in' operator
item_to_check = 60
if item_to_check not in my_list:
    print(f"{item_to_check} is not in the list.")
else:
    print(f"{item_to_check} is in the list.")