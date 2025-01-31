
def convert_temperature(temp, unit):
    if unit == 'C':
        return (temp * 9/5) + 32  # Convert Celsius to Fahrenheit if 'C' is given
    
    elif unit == 'F':
        return (temp - 32) * 5/9  # Convert Fahrenheit to Celcius if 'F' is given
    else: 
        return "Invalid unit. Indicate C or F."
    

def main():
    temp = float(input("Enter temperature: ")) # Get temperature from user
    unit = input("Enter unit of temperature (C or F): ")   # Get unit from user
    if unit == 'C': 
        print(f'Converting {temp}C to Fahrenheit:', convert_temperature(temp, unit))
    elif unit == 'F':
        print(f'Converting {temp}F to Celsius:', convert_temperature(temp, unit))
if __name__ == "__main__": # Call main() function if script is run directly
    main()