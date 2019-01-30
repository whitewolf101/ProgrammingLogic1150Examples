""" Uses random.shuffle and enumerate to
build and print a random movie playlist"""

import random

movies = ['Finding Nemo', 'Spiderman', 'Star Wars', 'The Godfather']

random.shuffle(movies)

for index, movie in enumerate(movies):
    print(f'{index+1}: {movie}')


