""" Writes a list to a file "data.txt".
Notice that the file is overwritten if it already exists."""


data = ['pizza', 'chips', 'nachos', 'soda']

all_data = '\n'.join(data)

f = open('data_joined_with_newlines.txt', 'w')
f.write(all_data)
f.close()
