""" Creating a directory and writing to a file in that directory. """

import os

try:
    os.makedirs('quotes')
except FileExistsError:
    pass    # ignore, the directory already exists


quote = """
"Every great developer you know got there by 
solving problems they were unqualified to solve until 
they actually did it." 
- Patrick McKenzie
"""

path = os.path.join('quotes', 'mckenzie.txt')

f = open(path, 'w')
f.write(quote)
f.close()


