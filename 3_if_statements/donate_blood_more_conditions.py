"""
To be a blood donor, you must be at least 16 years old, and weigh at least 110 lbs.
You also must be feeling well and healthy on the day you donate.
And, you can't donate blood if you have donated blood in the last 56 days.

This program asks the user these questions, and decides if they can give blood or not.

https://www.redcrossblood.org/donate-blood/how-to-donate/eligibility-requirements.html
"""

weight = float(input('Please enter your weight, in pounds: '))
age = int(input('Please enter your age, in years: '))

# Ask user if they are feeling well, and convert their answer to uppercase. If the user
# enters 'yes' then feeling_well will store the string 'YES'
feeling_well = input('Are you feeling well and healthy today? Enter "YES" if so: ').upper()

# Ask if they have donated recently, and convert to uppercase. An alternative is to ask the
# date of the last donation - but that would be a little more work to figure out if it was long enough ago.
donated_blood_recently = input('Have you donated blood in the past 56 days? Enter "YES" if so: ').upper()

# is the weight enough AND is the age enough AND is the user feeling well AND is the user NOT given blood recently?
                                                                             # Note != to check for inequality
if weight >= 110 and age >= 16 and feeling_well == 'YES' and donated_blood_recently != 'YES':
    print('Great! You are eligible to be a blood donor. ')
else:
    print('Sorry, you are not eligible today.')
