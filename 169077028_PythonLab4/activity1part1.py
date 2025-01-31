import random
def roll_dice(num_dice, num_sides):
    total = 0
    for i in range(num_dice):
        total += random.randint(1, num_sides)
        #use randint() to generate a random number between 1 and num_sides
    return total
print('Rolling 3 dice with 6 sides each:',roll_dice(3, 6))