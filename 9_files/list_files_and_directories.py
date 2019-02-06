""" List all of the current files and directories in a path """

import os

listing = os.listdir('.')
for item in listing:
    print(item)

