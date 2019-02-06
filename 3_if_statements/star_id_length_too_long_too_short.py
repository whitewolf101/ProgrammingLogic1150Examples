"""Checking if a StarID is exactly 8 characters, or too long, or too short """

star_id = input('Please enter your StarID: ')

if len(star_id) == 8:
    print('Your StarID is the correct length.')
elif len(star_id) > 8:
    print('Your StarID is more than 8 characters - too long')
else:
    print('Your StarID is less than 8 characters - too short')
