parking_time = float(input('How many hours have you parked? '))

# The max parking time allowed is 2 hours.

# Try using > instead of >= in the comparison. How does the program behave differently?
# for example, what does it do at 2 hours?

if parking_time >= 2:
    print('Warning! You should move your car.')
else:
    print('You are ok for parking, you still have time.')

print('This is the end of the program.')

