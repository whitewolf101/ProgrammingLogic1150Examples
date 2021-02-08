"""
A program to calculate a bus fare.
On a city bus, the fare depends on your age.

Children 5 and younger ride free.
Children 6-16 pay $0.50
Adults, 16 and over pay $2
Seniors 65 and over pay $1.

This program uses if, elif and else to decide the correct fare based on a user's age.

"""

age = int(input('Please enter your age as a whole number: '))

if age <= 5:
    print('The bus fare for passengers 5 and under is $0.00')
elif age <= 16:  # this is only checked if age <= 5 was false (if age is greater than 5), so we don't also have to check if age is less than 5.
    print('The bus fare for passengers between 6 and 16 is $0.50')
elif age < 65:   # this is only checked if age wasn't less than or equal to 5 and age wasn't less than or equal to 16
    print('The bus fare for passengers over 16 but younger than 65 is $2.00')
else:
    print('The bus fare for passengers 65 and older is $1.00')
