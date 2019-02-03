""" Using upper() or lower() to compare strings in a case-insensitive way """

print('Quiz program!')

print('What number system do computers use?')  # Binary

answer = input('What is your answer? ')

if answer.lower() == 'binary':
    print('Correct!')
else:
    print('Sorry, the answer is binary.')



if answer.upper() == 'BINARY':
    print('Correct!')
else:
    print('Sorry, the answer is binary.')


