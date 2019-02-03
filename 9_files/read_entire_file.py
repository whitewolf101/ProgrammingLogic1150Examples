""" Read the entire file
 What problem could there be if the file is really, really large? """


with open('data.txt', 'r') as f:
    data = f.read()  # data is a single string with the entire file in it

print(data)
