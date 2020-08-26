""" Testing if a number is within a range """

number_of_credits = int(input('How many credits you are taking this semester? '))

# A valid number of credits must be between 0 and 24.
# When you run this program, try -10, 0, 10, 24, 100 to test it.

if number_of_credits >= 0 and number_of_credits <= 24:
    print('Thank you, you are taking ' + str(number_of_credits) + ' credits')
else:
    print(str(number_of_credits) + ' is not a valid number of credits')

