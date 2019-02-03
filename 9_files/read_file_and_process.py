""" Reads the hours_worked file and processes the data to calculate total hours worked """

hours_worked = {}

with open('hours_worked.data') as f:
    for line in f:
        data = line.split(':')
        day = data[0]
        hours = int(data[1])
        hours_worked[day] = hours


print(hours_worked)
total_hours = sum(hours_worked.values())
print(f'Total hours worked this week: {total_hours}')
