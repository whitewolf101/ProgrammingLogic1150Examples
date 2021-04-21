from datetime import date

# What is today' date? This is read from your computer's clock
today = date.today()
print(f'Today is {today}')

# Example year, month, day
year = 2996
month = 10
day = 6

# Create another date. Note the order of the arguments
date_object = date(year, month, day)
print(f'Example date object is {date_object}')

# Dates can be compared with operators like == and != and < and >
if date_object > today:  # if date_object is greater than today, it's in the future
    print('The date object is in the future compared to today')
else:
    print('The date object is in the past compared to today')
