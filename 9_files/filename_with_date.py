""" Writes to a file with the current date and time in the filename"""

from datetime import datetime
import shelve

now = datetime.now()
now_string = now.strftime("%d_%h_%y")
print(now_string)

pokemon = {'Pikachu': 6, 'Eevee': 6.5}

# Writes to a file with a name in the format 03_Feb_19_exchange_rates.txt
# with open(f'{now_string}_exchange_rates.txt', 'w') as f:
#     shelve.

filename = f'{now_string}_pokemon.txt'


shelve_file = shelve.open(filename)
shelve_file['pokemon'] = pokemon
shelve_file.close()  # Remember to close your shelf

# Read data - this would work if the program was closed and re-opened.

shelve_file = shelve.open(filename)
print(shelve_file['pokemon'])
