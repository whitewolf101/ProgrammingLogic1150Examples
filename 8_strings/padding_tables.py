""" Padding with spaces """

hours_worked = {
    'Monday': 4.3,
    'Tuesday': 12,
    'Wednesday': 11.6,
    'Thursday': 3,
    'Friday': 9}

# Table heading
print(f'{"Day":<15}{"Hours Worked":<15}')

# Table data from dictionary
for day, hours in hours_worked.items():
    print(f'{day:<15}{hours:<15}')


