""" Examples for formatting numbers in format strings """


import math

pi = math.pi
print(f'pi to 3 decimal places is {pi:.3f}')



miles_to_chicago = 408
km_to_chicago = miles_to_chicago * 1.60934

print(f'It is {miles_to_chicago} miles from Minneapolis to Chicago')
print(f'It is {km_to_chicago:.1f} kilometers from Minneapolis to Chicago')

