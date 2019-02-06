""" Creating a directory """

import os

try:
    os.makedirs('quotes')
except FileExistsError:
    print('The quotes directory already exists.')


