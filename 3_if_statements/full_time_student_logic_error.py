"""
if, elif, else Enrollment status at Minneapolis College is defined as the following:

Full time: 12 or more credits
Half time: 6-11 credits
Less than half time: 1-5 credits

BUT this program doesn't work as expected. What does it print if you enter 7

"""

number_of_credits = int(input('How many credits you are taking this semester? '))

# This if - elif - else statement doesn't work as expected. Can you see why?
# Try with 15 credits - it doesn't print the right answer.

if number_of_credits >= 6:
    print('You are a half-time student')
elif number_of_credits >= 12:
    print('You are a full-time student')
else:
    print('You are less than half-time')



