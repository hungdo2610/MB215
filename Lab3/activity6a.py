for variable in range(2, 20):
    if variable % 2 == 0:
        print(variable)
#Loop with ‘range()’ to iterate through and print even numbers.

for variable in range(1,3):
    
    # Outer loop for numbers 1 to 3
for i in range(1, 4):
    print(f"Multiplication table for {i}:")
    # Inner loop for range 1 to 10
    for j in range(1, 11):
        # Calculate the product
        product = i * j
        # Print the multiplication expression and result
        print(f"{i} x {j} = {product}")
    # Print a blank line after each table for better readability
    print()
