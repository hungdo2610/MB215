## Activity 10. Save a list to a file
# Function to save a list to a file

def save_list_to_file(file_name, input_list):
    with open(file_name, 'w') as file:
        file.writelines(f"{item}\n" for item in input_list)

# Function to read data from a file and return it as a list
def read_list_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return [line.strip() for line in file.readlines()]#line.strip() is a string method used to remove leading and trailing whitespace characters (such as spaces, tabs, and newline characters) from a string
    except FileNotFoundError:
        return []

# Original list
original_list = ['Apple', 'Banana', 'Cherry', 'Date']

# File name to save and read data
file_name = 'fruits.txt'

# Save the list to a file
save_list_to_file(file_name, original_list)

# Read data from the file
read_data = read_list_from_file(file_name)

# Print the read data
print("Data read from the file:", read_data)
