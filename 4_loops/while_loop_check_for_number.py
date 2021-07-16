"""
What if your program expects a numeric value, for example,

number = int(input('Please enter a number: '))

and a user types in 'cat' or
something that is not a number?

The program will crash with a message like this,

Please enter a number: cat
Traceback (most recent call last):
  File "while_loop_check_for_number.py", line 10, in <module>
    number = int(input('Please enter a number: '))
ValueError: invalid literal for int() with base 10: 'cat'

Python can't convert 'cat' to an int so it "raises an exception" which
means that the program is reporting an error that it can't deal with.

And when a program experiences an error it can't deal with, it crashes and
displays an error message.

It's possible to anticipate and "catch" handle this type of error/exceptions
in your program. In this case, we'd like to allow the user to try again.

"""

# Try to ask user for input... but anticipate there may be an error.
# this is a basic try-except structure. If the user doesn't enter
# a number, they don't get to try again.
try:
    number_1 = int(input('Please enter an integer number. You only get one chance: '))
    # if the user enters a number, it will be stored in the variable
    # number and your program can use it.
    print(f'Thank you for entering the number {number_1}')
except ValueError:
    # if the user doesn't enter a number, the line with int() in raises
    # A ValueError exception and then this block of code will run.
    print('That was not an integer number')


# How about allowing the user to try again? Use a while loop.

while True:
    try:
        number_2 = int(input('Please enter an integer number. You have as many tries as you need to enter a number: '))
        # if the user enters a number, it will be stored in the variable
        # number and your program can use it.
        print(f'Thank you for entering the number {number_2}')
        break   # we have a number, no need to repeat the loop
    except ValueError:
        # if the user doesn't enter a number, the line with int() in raises
        # A ValueError exception and then this block of code will run.
        print('That was not an integer number. Try again.')
        # since we are in a while True loop, the loop will repeat and ask the user for input again.

print(f'Number 1 was {number_1}')  # What value does this have if you enter 'cat' for the number 1? You'll see a different error on this line.
print(f'Number 2 was {number_2}')  # What value does this have? Are we guaranteed to have a value?
