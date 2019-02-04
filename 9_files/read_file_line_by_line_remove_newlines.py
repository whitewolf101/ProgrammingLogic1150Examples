""" Read the entire file, one line at a time.
This approach is better if the file size is unknown or may be large.
Your program only has to store one line in memory at once. """


f = open('planets.txt', 'r')
for line in f:
    line = line.rstrip()
    print(line)

f.close()


