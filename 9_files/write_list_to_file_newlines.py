""" Writes a list to a file "data.txt".
Notice that the file is overwritten if it already exists."""


data = ['pizza', 'chips', 'nachos', 'soda']

f = open('data_newlines.txt', 'w')
for line in data:
    f.write(line)
    f.write('\n')
