"""
Escape characters

\t \n \' \" \\  \b
"""


# Tabs
print('There is a tab at the end of this line.\t Can you see it in the output?')

# Example:
credits_per_day = {'Monday': 4, 'Tuesday': 0, 'Wednesday': 2, 'Thursday': 0, 'Friday': 3}
for day, credits in credits_per_day.items():
    print(f'{day}\t{credits} credits')


# Aside: but string formatting to pad with spaces will look tidier for tabular output
print()
for day, credits in credits_per_day.items():
    print(f'{day:10} {credits} credits')


print()

# Newlines
print('One line\nAnother line')

print()

# Quotes
print('Macy\'s is a department store.')
print('"Where\'s my book?", she said.')   # Escape single quotes in a single quoted string
print("\"Where's my book?\", she said.")  # In a double quoted string, need to escape double quotes

print()

# Backslash
print('To include a tab in a string, use the \\t escape code')

print()

# Not all escape characters are converted to a printed character.
print('123\b456')  # What does this print? What's missing?

