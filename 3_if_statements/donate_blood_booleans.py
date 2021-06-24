"""
To be a blood donor, you must be at least 16 years old, and weigh at least 110 lbs.
This program asks the user for their age and weight,
and decides if they can give blood or not.

This program assumes a user can donate blood using a boolean set to True.
It checks the various requirements, and if the user is found to be ineligible, the
boolean is set to false.

At the end of the program, the value of the boolean is used to print a message to the user.

"""

eligible = True  # Assume the user is eligible.

weight = float(input('Please enter your weight, in pounds: '))
age = int(input('Please enter your age, in years: '))

# check each requirement in turn

if weight < 110:
    # print reason why user is not eligible
    print('Sorry, you do not weigh enough. For the safety of donors, you must weigh at least 110 lbs.')
    # set the eligible boolean variable to false
    eligible = False

if age < 16:
    # print reason why user is not eligible
    print('Sorry, you are not old enough. Please come back when you are 16 or older.')
    # set the eligible boolean variable to false
    eligible = False

# We could include more checks here. Other checks that are made in a real-world situation
# include recent foreign travel, and certain medical conditions.

# check the eligible boolean. If it was not changed to False, the user meets all the conditions.

if eligible:
    print('Great! You are eligible to be a blood donor. Thank you!')
else:
    print('Sorry, you are not eligible. Please see the reason(s) displayed above.')
