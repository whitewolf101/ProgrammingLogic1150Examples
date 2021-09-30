""" A dice rolling program where you can customize the type of dice, and the number
of dice to roll.

Some possible enhancements to this program:

1. Make sure the number of sides is at least 1
2. Allow the user to roll their dice again
3. If the user rolls again, can you let them change the number of sides and/or the number of dice rolled?

"""

import random


def main():
    print('Welcome to the dice rolling program.')
    print('This program can roll regular 6-sided dice, or dice with any number of sides.')

    print('What kind of dice would you like to roll? Enter the number of sides for your dice.')
    dice_sides = int(input('Enter number of sides: '))

    print('How many dice would you like to roll?')
    dice_count = int(input('Enter number of dice: '))

    print('Let\'s roll the dice!')

    roll_dice(dice_sides, dice_count)  # call function with two arguments.
    # Notice that the argument names do not need to be the same as the function parameter names.


def roll_dice(max_dice_value, number_of_dice):
    """
    Roll the given number of dice and print the values rolled.
    Paramters:
        max_dice_value: The highest number this dice can roll.
            For example, if the user wishes to roll a regular 6-sided dice, set max_dice_value to 6
            If the user wishes to roll a 20-sided dice, set max_dice_value to 20.
        number_of_dice: How many dice to roll. All dice are assumed to have the same maximum value.
    """
    # repeat the loop once time for each dice
    for dice in range(number_of_dice):
        # generate a random number between 1 and max_dice_value
        # for example, if the user wishes to roll a regular 6-sided dice, set max_dice_value to 6
        dice_value = random.randint(1, max_dice_value)
        print(f'You rolled a {dice_value}')


main()