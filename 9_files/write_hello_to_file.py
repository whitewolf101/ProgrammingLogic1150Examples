""" Writes "hello" to the file "hello.txt".
Notice that the file is overwritten if it already exists."""

with open('hello.txt', 'w') as f:
    f.write('hello')
