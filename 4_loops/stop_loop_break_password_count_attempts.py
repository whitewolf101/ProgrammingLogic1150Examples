"""
Enter password. Stop loop using break if password is correct
User is only allowed 4 attempts to get the password right.
"""

secret_password = 'kittens'
attempts = 0  # use this variable to count the number of attempts

while True:
    password = input('Please enter the password: ')
    attempts = attempts + 1  # add 1 to the number of attempts
    if secret_password == password:  # correct password!
        break  # End the loop
    elif attempts >= 4:  # too many attempts
        print('Wrong password. You have exceeded the number of attempts.')
        break  # end loop
    else:   # wrong password but less than 4 attempts, can try again
        print('Error - wrong password. Try again.')


# Once the loop has ended, check if the password was entered correctly
if password == secret_password:
    print('Welcome, authorized user.')
else:
    print('Access denied.')
