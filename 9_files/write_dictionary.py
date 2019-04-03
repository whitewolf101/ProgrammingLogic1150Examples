"""
Write all the data from a dictionary to a file.
"""


favorites = {
    'food': 'pizza',
    'color': 'green',
    'band': 'REM'
}

f = open('favorites.txt', 'w')
for key, value in favorites.items():
    f.write(f'Your favorite {key} is {value}.\n')
f.close()