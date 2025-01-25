input('Is it sunny outside?')
input('Is it the weekend?')
# Step 1: Declare two Boolean variables
is_sunny = 'Yes'
is_weekend = 'No'

# Step 2: Demonstrate logical operations (AND, OR, NOT)
# Logical AND
both_conditions = is_sunny and is_weekend
print(f"Is it sunny AND the weekend? {both_conditions}")

# Logical OR
either_condition = is_sunny or is_weekend
print(f"Is it sunny OR the weekend? {either_condition}")

# Logical NOT
not_sunny = not is_sunny
print(f"Is it NOT sunny? {not_sunny}")


# Conditional statement with logical operation
if is_sunny and not is_weekend:
    print("It's sunny but not the weekend. Time to enjoy some fresh air!")
elif is_sunny and is_weekend:
    print("It's sunny and the weekend. Perfect for a getaway!")
elif not is_sunny and is_weekend:
    print("It's the weekend, but it's not sunny. Maybe stay indoors.")
else:
    print("Neither sunny nor the weekend. Focus on work or study!")





