""" Append lines to a file. If the file doesn't exist, it will be created.
 If the file does exist, the new data will be added to the end of the file. """


f = open('planets.txt', 'a')  # 'a' for append mode
f.write('Hello Jupiter\n')
f.write('Hello Saturn\n')
f.close()

