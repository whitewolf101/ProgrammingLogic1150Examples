""" When reading a file, it is an error if the file does not exist. """

try:
    f = open('does_not_exist.txt', 'r')
    data = f.read()  # data is a single string with the entire file in it
    f.close()
    print(data)
except FileNotFoundError:
    print('Error - file does not exist')
