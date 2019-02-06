""" When reading a file, it is an error if the file does not exist. """

try:
    f = open('does_not_exist.txt', 'r')
    lines = f.readlines()
    f.close()
    print(lines)
except FileNotFoundError:
    print('Error - file does not exist')


