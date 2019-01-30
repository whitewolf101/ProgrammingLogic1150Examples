winter_months = ['October', 'November', 'December', 'January', 'February', 'March', 'April']  # sigh

snowfall = {}

for month in winter_months:
    snow = float(input(f'How much snow in {month}, in inches? '))
    snowfall[month] = snow

print()
print('Here is all of the data you entered:')

for month, snow in snowfall.items():
    print(f'In {month} there was {snow} inches of snow.')

# Analysis: what's the total amount of snow?

total_snow = sum(snowfall.values())

# Average snowfall per month - the total divided by the number of months
months = len(snowfall)
average = total_snow / months

print()
print(f'The total amount of snow in {months} months is {total_snow} inches.')
print(f'The average amount of snow per month is {average:.2f} inches')
