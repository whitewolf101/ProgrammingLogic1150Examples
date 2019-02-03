""" Read the entire file, one line at a time.
This approach is better if the file size is unknown or may be large.
Your program only has to store one line in memory at once. """


with open('data.txt', 'r') as f:
    for line in f:
        print(line)

