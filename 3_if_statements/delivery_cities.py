"""
if elif else example

A company can deliver to Minneapolis, St Paul and Bloomington.  It does
not deliver to any other cities.

This program uses if elif else to decide if a city is one that the
company delivers to, or not.

"""

# Example city - try changing this to 'Minneapolis' or 'St Paul' or 'St Louis Park'.
# What does the program do?
city = 'Woodbury'

if city == 'Minneapolis':
    print('We can deliver to you in Minneapolis!')
elif city == 'St Paul':
    print('We can deliver to you in St Paul!')
elif city == 'Bloomington':
    print('We can deliver to you in Bloomington!')
else:
    print('Sorry, can\'t deliver to your city')

# TODO - a question for you. The company can also deliver to Roseville.
# Can you add another elif ?
# So program should say it can deliver to Roseville
# but not to other cities, like St Louis Park or Anoka.
