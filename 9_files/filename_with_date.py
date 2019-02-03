""" Writes to a file with the current date and time in the filename"""

from datetime import datetime


now = datetime.now()
now_string = now.strftime("%d_%h_%y_%I%M%p")

# Writes to a file with a name in the format 03_Feb_19_1046AM_file.txt
with open(f'{now_string}_file.txt', 'w') as f:
    f.write('hello')
