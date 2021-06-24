""" Program to decide what activity and what clothes to wear based on the season. """

month = input('What month is it? ')

# Create a boolean variable to represent if it is summer or not.
# We'll say summer is June, July, or August.

if month == 'June' or month == 'July' or month == 'August':
    is_summer = True  # True, for yes, it is summer
else:
    is_summer = False  # False, for no, it is not summer

# Now we know if it is summer or not, based on the value of the is_summer boolean variable
# So if we need to make a decision based on summer or not, we can use the is_summer variable
# instead of having to check if month is 'June' or 'July' or 'August'

# Let's decide what type of hat to wear
if is_summer:
    print('It is summer! Wear a sun hat.')
else:
    print('It is not summer. Wear a warm hat.')

# what if we need to make another decision based on summer or not?

if is_summer:   # use our boolean, instead of checking if June, July, or August. Much simpler!
    print('It is summer! You can go swimming.')
else:
    print('It is not summer. You can go skiing.')


