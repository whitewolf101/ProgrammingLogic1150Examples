import shelve

filename = 'hoursworked.data'
hours_key = 'hours_worked'

shelf = shelve.open(filename)
hours_worked = shelf.get(hours_key)  # Returns None if key not found
shelf.close()

if not hours_worked:
    hours_worked = {}

day = input('What day is it?')
hours = float(input(f'How many hours did you work on {day}?'))

hours_worked[day] = hours

print('Thank you. Here is all of your data:')

for day, hours in hours_worked.items():
    print(f'On {day} you worked {hours} hours.')


shelf = shelve.open(filename)
shelf[hours_key] = hours_worked
shelf.close()

