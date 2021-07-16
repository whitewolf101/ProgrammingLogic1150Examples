""" Create and use function to handle getting and validating an integer number
Create and use a function to handle getting and validating a float number.
 These functions are very general and could be used exactly as written in many other programs. """


def main():
    # How many times did you ride the bus?
    number_of_rides = int_number_input('How many times did you ride the bus this week? ')
    cost_of_bus_ride = float_number_input('What does one ride cost? ')
    total = number_of_rides * cost_of_bus_ride
    print(f'You rode the bus {number_of_rides} times, each ride costs ${cost_of_bus_ride} so your total expense was ${total}.')


def int_number_input(question):
    while True:
        try:
            number = int(input(question))  # Ask the question, convert to int and store in variable
            # if the user enters a number, it will be stored in the variable
            # number and your program can use it.
            return number  # returning from a while loop ends the loop.
        except ValueError:
            # if the user doesn't enter a number, the line with int() in raises
            # A ValueError exception and then this block of code will run.
            print('Please enter an integer number. Try again.')
            # since we are in a while True loop, the loop will repeat and ask the user for input again.


def float_number_input(question):
    while True:
        try:
            number = float(input(question))  # Ask the question, convert to float and store in variable
            # if the user enters a number, it will be stored in the variable
            # number and your program can use it.
            return number  # returning from a while loop ends the loop.
        except ValueError:
            # if the user doesn't enter a number, the line with int() in raises
            # A ValueError exception and then this block of code will run.
            print('Please enter a number. Try again.')
            # since we are in a while True loop, the loop will repeat and ask the user for input again.

main()