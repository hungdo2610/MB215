#Activity 1. Define a list with different types of elements

my_list = [1, "two", 3.0, True]
# Print the entire list
print("The entire list:", my_list)
# Convert a tuple to a list using the list() function
#Tuples are defined by enclosing the elements within parentheses () instead of square brackets [] used by lists.
my_tuple = (4, "five", 6.0, False)
tuple_to_list = list(my_tuple)
# Print the converted list
print("Converted list from tuple:", tuple_to_list)