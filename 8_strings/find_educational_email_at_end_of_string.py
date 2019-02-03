"""
Find function
compare to the in operator
Use this if you need to know where in a string the text is .
"""

email = input('Enter your email: ')
if email.endswith('.edu'):
    print('This is a student email')
else:
    print('This is not a student email.')

