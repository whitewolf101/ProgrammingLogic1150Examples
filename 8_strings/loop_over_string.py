""" Strings are iterable. Can access each character in turn with a loop. """


phone = 'Android'
for letter in phone:
    print(letter)


# Prints as a triangle - each letter is repeated one more time than the last.
for index, letter in enumerate(phone):
    print(letter * (index+1))


college = 'Minneapolis College'

for letter in college:
    print(letter)

