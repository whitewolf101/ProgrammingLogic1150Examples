""" Read the entire file
 What problem could there be if the file is really, really large? """


f = open('data.txt', 'r')
data = f.read()  # data is a single string with the entire file in it
f.close()

print(data)
