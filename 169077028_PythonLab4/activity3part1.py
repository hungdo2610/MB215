import random

def generate_random_number(min_val, max_val):
    return random.randint(min_val, max_val) # Generates a random number between min_val and max_val

  # Generates a random number between 1 and 10
print(f"The generated random number is: {generate_random_number(1, 10)}")


