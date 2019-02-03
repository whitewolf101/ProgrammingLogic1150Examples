""" Writes a list to a file "data.txt".
Notice that the file is overwritten if it already exists."""


data = ['pizza', 'chips', 'nachos', 'soda']

# What does the file look like? Is it as you expected?
with open('data.txt', 'w') as f:
    f.writelines(data)
