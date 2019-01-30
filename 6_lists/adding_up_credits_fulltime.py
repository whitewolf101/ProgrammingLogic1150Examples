""" Imagine you have a list of the credits for each class you are taking. """

credits_per_class = [3, 2, 2, 4]

total = 0

for credits in credits_per_class:
    total = total + credits

print(f'The total number of credits is {total}')

if total >= 12:
    print('You are a full-time student.')
elif total >= 6:
    print('You are a part-time student.')
else:
    print('You are less than part-time.')

