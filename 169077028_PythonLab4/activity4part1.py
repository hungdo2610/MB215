import random

def simulate_investment(amount, years, rate_min, rate_max):
    for i in range(years):  
        rate = random.uniform(rate_min, rate_max)  # Generate a random interest rate
        amount += amount * (rate / 100)  # Apply the interest

    return round(amount, 2)  # Return the final amount rounded to 2 decimal places

def main():
    initial_amount = float(input("Enter initial investment amount: "))  # Get initial investment amount from user
    investment_years = int(input("Enter number of years to invest: "))  # Get number of years to invest from user
    min_rate = float(input("Enter minimum interest rate: "))  # Get minimum interest rate from user
    max_rate = float(input("Enter maximum interest rate: "))  # Get maximum interest rate from user

    final_amount = simulate_investment(initial_amount, investment_years, min_rate, max_rate)
    print(f"Final investment value after {investment_years} years: ${final_amount}")

# Ensures the script runs only when executed directly
if __name__ == "__main__":
    main()
