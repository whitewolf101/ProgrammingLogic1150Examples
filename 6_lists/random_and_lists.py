""" Using random methods with a list
Selecting a list item at random
Shuffling a list
"""


import random

playlist = ['Prince', 'Daft Punk', 'Led Zeppelin', 'Lady Gaga', 'Rhianna', 'Beyonce']

# Pick a random item from the list
print(random.choice(playlist))


# Shuffle a list
random.shuffle(playlist)
print(playlist)

