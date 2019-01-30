""" Using remove. To use remove, you need to know the thing you are removing."""

rooms = ['T.3010', 'T.3020', 'T.3030', 'T.3040', 'T.3050', 'T.3080']

rooms.remove('T.3020')
print(rooms)        # ['T.3010', 'T.3030', 'T.3040', 'T.3050', 'T.3080']

rooms.remove('T.3080')
print(rooms)        # ['T.3010', 'T.3030', 'T.3040', 'T.3050']

# This will error, M.1400 is not in the list
# rooms.remove('M.1000')

""" If there is more than one of the thing in the list, only the first one will be removed. """

numbers = [4, 6, 1, 9, 10, 3, 6, 4, 6]   # More than one 6 in the list

numbers.remove(6)   # Only the first 6 is removed
print(numbers)     # [4, 1, 9, 10, 3, 6, 4, 6]

