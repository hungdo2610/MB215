def calculate_ontario_tax(income):
    # Define tax brackets and rates based on Ontario's tax table
    brackets = [49220, 98407, 150000, 220000]
    rates = [0.0505, 0.0915, 0.1116, 0.1216, 0.1316]

    # Calculate tax based on brackets
    tax = 0
    previous_bracket = 0

    for i in range(len(brackets)):
        if income <= brackets[i]:
            tax += (income - previous_bracket) * rates[i]
            break
        else:
            tax += (brackets[i] - previous_bracket) * rates[i]
            previous_bracket = brackets[i]
    else:
        tax += (income - previous_bracket) * rates[-1]

    return tax

def main():
    try:
        income = float(input("Enter your taxable income: "))
        tax = calculate_ontario_tax(income)
        print(f"Your tax amount is: ${tax:.2f}")
        
        paid_tax = float(input("Enter the tax amount you have already paid: "))
        balance = tax - paid_tax
        
        if balance < 0:
            print(f"You are entitled to a refund of: ${-balance:.2f}")
        else:
            print(f"You owe an additional tax of: ${balance:.2f}")
    
    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    main()
