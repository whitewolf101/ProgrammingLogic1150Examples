"""
Enter password. Stop loop using a condition if password is correct
"""

secret_password = 'kittens'
password = input('Please enter the password: ')

while secret_password != password:
    print('Error - wrong password. Try again.')
    password = input('Please enter the password: ')


# The only way to end the loop above is if the password is correct.
print('Welcome, authorized user')
