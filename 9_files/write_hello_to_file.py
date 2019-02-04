""" Writes "hello" to the file "hello.txt".
Notice that the file is overwritten if it already exists."""

f = open('hello.txt', 'w')
f.write('hello')
f.close()


