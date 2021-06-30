"""
To be a blood donor, you must be at least 16 years old, and weigh at least 110 lbs.
This program asks the user for their age and weight,
and decides if they can give blood or not.

The problem with this approach is that it works ok for two checks, but we'd need
to write a lot more conditions if there were more things to check for - like a donor
must be feeling well and healthy. You can't donate blood again if you've donated blood
in the last 56 days.

https://www.redcrossblood.org/donate-blood/how-to-donate/eligibility-requirements.html
"""

weight = float(input('Please enter your weight, in pounds: '))
age = int(input('Please enter your age, in years: '))

if weight >= 110 and age >= 16:
    print('Great! You are eligible to be a blood donor. ')
elif weight >= 110 and age < 16:
    print('Sorry, you are not old enough. Please come back when you are 16 or older.')
elif weight < 110 and age >= 16:
    print('Sorry, you do not weigh enough. For the safety of donors, you must weigh at least 110 lbs.')
else:
    print('Sorry, you are too young and do not weigh enough to give blood. ')
    print('Please come back when you are 16 or older, and weigh at least 110 lbs.')
