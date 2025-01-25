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
