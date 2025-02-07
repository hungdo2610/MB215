##Activity 9. Copying Lists
# Original list

original_list = [1, 2, 3, 4, 5]

# Method 1: Using a for loop to create a copy
copied_list1 = []
for item in original_list:
    copied_list1.append(item)

# Print the copied list
print("Method 1: Copied list using a for loop:", copied_list1)
# Original list
original_list = [1, 2, 3, 4, 5]

# Method 2: Concatenating the old list to create a copy
copied_list2 = [] + original_list

# Print the copied list
print("Method 2: Copied list using concatenation:", copied_list2)

# We can do some calculatuion on the list. Calculate the total of numeric values in the copied list
# Original list
original_list = [1, 2, 3, 4, 5]

# Create a copy of the original list
copied_list = list(original_list)

# Calculate the total of numeric values in the copied list
total = sum(item for item in copied_list)

# Calculate the average of numeric values in the copied list
average = total / len(copied_list) if copied_list else 0

# Print the total and average
print("Total of numeric values in the copied list:", total)
print("Average of numeric values in the copied list:", average)
