Name = input('What is your name?')
Age = int(input('How old are you?'))
import datetime
today = datetime.datetime.now()
year = today.year
birth_year = year - Age
print(f"Hello, {Name}! You were born in {birth_year}.")