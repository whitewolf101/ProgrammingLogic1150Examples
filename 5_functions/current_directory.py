""" A Python library function that takes no parameters (input) and has a return value (output) """

import os  # Python library containing various operating system related functions


# The library function os.getcwd() takes no parameters
# and returns the current working directory
# This is typically the directory containing the python project.
cwd = os.getcwd()
print('The current directory is ' + cwd)

