"""
Roll many dice, and store values in a list.
"""

import random

dice_values = []  # empty list

number_of_dice = int(input('How many dice to roll? '))

for dice in range(number_of_dice):
    dice_roll = random.randint(1, 6)  # roll a dice
    dice_values.append(dice_roll)  # add that dice value to the list

# display all the dice rolls
print(f'The dice rolls are {dice_values}')

# alternative: display the values individually
for index, dice_roll in enumerate(dice_values):  # a loop for each item in the dice_values list
    print(f'Dice {index + 1} rolled a {dice_roll}')
