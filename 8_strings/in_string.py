"""
Compare to the find() method
in just tells you if the search string is in your string
"""

message = 'Hello, python programmers!'

print('python' in message)  # True

if 'python' in message:
    print('The message is for python programmers')
else:
    print('The message is not for python programmers')


if 'java' in message:
    print('The message is for java programmers')
else:
    print('The message is not for java programmers')



classes = ['ITEC 1150', 'BTEC 1245', 'ENGL 1100']

for c in classes:               # We can't use for class in classes:  because 'class' is a reserved word in Python.
    if 'ITEC' in c:
        print(f'{c} is an ITEC class')
    else:
        print(f'{c} is not an ITEC class')
