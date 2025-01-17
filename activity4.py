# Ask the user for column titles
print("Enter column titles for the table (maximum of 20 characters each).")
col1 = input("Enter title for Column 1: ")[:20]
col2 = input("Enter title for Column 2: ")[:20]
col3 = input("Enter title for Column 3: ")[:20]

# Ask for data to populate the table
print("\nNow, enter data for each row (max 20 characters per field). Type 'done' to finish.")
rows = []
while True:
    data1 = input("Enter data for Column 1: ")[:20]
    if data1.lower() == 'done':
        break
    data2 = input("Enter data for Column 2: ")[:20]
    data3 = input("Enter data for Column 3: ")[:20]
    rows.append((data1, data2, data3))

# Print the formatted table
print("\nFormatted Table:")
print(f"{col1:<20} | {col2:<20} | {col3:<20}")
print("-" * 66)  # Line separator
for row in rows:
    print(f"{row[0]:<20} | {row[1]:<20} | {row[2]:<20}")
