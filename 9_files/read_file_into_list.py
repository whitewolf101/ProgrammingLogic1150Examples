""" Read the entire file into a list
 What problem could there be if the file is really, really large? """


with open('data.txt', 'r') as f:
    lines = f.readlines()

print('All of the lines from the file:')
print(lines)

print('All the lines, one by one: ')
for line in lines:
    print(line)
