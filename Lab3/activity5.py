# Initiate
total_sum = 0
count = 0

# Start the while loop
while total_sum < 100:
    # Prompt the user for input
    user_input = input('Enter a number or press Space to stop: ')
    
    # ' ' to exit
    if user_input == ' ':
        break
    
    # Try to convert the input to an integer
    try:
        number = int(user_input)
        # Add the number to the total sum
        total_sum += number
        # Increment the count
        count += 1
    except ValueError:
        print("Invalid input. Please enter a number or press Space to stop.")

# Display the results
print(f"\nTotal sum: {total_sum}")
print(f"Count of numbers entered: {count}")

    



