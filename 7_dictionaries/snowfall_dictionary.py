winter_months = ['October', 'November', 'December', 'January', 'February', 'March', 'April']  # sigh

snowfall = {}

for month in winter_months:
    snow = float(input(f'How much snow in {month}, in inches? '))
    snowfall[month] = snow

print('Here is all of the data you entered:')

for month, snow in snowfall.items():
    print(f'In {month} there was {snow} inches of snow.')
