""" Writes a list to a file "data.txt".
Notice that the file is overwritten if it already exists."""


data = ['pizza', 'chips', 'nachos', 'soda']

all_data = '\n'.join(data)

with open('data_joined_with_newlines.txt', 'w') as f:
    f.write(all_data)
