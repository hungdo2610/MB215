### Activity 12. tTwo-dimensional list
# Create a two-dimensional list (3x3 matrix)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Print the two-dimensional list
print("Two-dimensional list (matrix):")
for row in matrix:
    print(row)

# Accessing elements in the two-dimensional list
element_00 = matrix[0][0]  # Row 0, Column 0
element_12 = matrix[1][2]  # Row 1, Column 2
element_21 = matrix[2][1]  # Row 2, Column 1

print("\nAccessed elements:")
print(f"Element at [0][0]: {element_00}")
print(f"Element at [1][2]: {element_12}")
print(f"Element at [2][1]: {element_21}")

# Processing data in the two-dimensional list using nested loops
print("\nProcessed data:")
for row in matrix:
    for element in row:
        print(element, end=' ') #Each number is printed on the same line with spaces between them due to the end=' ' argument in the print() function.
    print()  # Print a newline after each row
