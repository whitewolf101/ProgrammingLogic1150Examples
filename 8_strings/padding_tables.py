""" Padding with spaces """

hours_worked = {'Monday': 4.3, 'Tuesday': 12, 'Wednesday': 11.6, 'Thursday': 3, 'Friday': 9}

avg_hours = sum(hours_worked.values()) / len(hours_worked)

print(f'On average you worked {avg_hours:.2f} hours per day')

# No spacing
for day, hours in hours_worked.items():
    print(f'On {day} you worked {hours} hours')

print()

# Table - can be easier to read

# Table heading
print(f'{"Day":<15}{"Hours Worked":<15}')

for day, hours in hours_worked.items():
    print(f'{day:<15}{hours:<15}')
