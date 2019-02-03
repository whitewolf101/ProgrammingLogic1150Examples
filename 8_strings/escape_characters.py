"""
Escape characters

\t \n \' \" \\  \b
"""

# Quotes. If you only have one type of quote, use the other type to create the string.
print("Macy's is a department store.")      # Single quote in double quoted string
print('He said "Code looks good!" to me.')  # Double quote in single quoted string


print("\"Where's my book?\", she said.")  # In a double quoted string, need to escape double quotes
print('"Where\'s my book?", she said.')   # Escape single quotes in a single quoted string

# Single quotes
print('Macy\'s is a department store.')

# Newlines
print('One line\nAnother line')

# Tabs
print('There is a tab at the end of this line.\t Can you see it in the output?')

# Backslash
print('Your file is at C:\\Users\\document.doc')

print('To include a tab in a string, use the \\t escape code')

# Example:
# Note that string formatting to pad with spaces will look tidier for tabular output
credits_per_day = {'Monday': 4, 'Tuesday': 0, 'Wednesday': 2, 'Thursday': 0, 'Friday': 3}
for day, credits in credits_per_day.items():
    print(f'{day}\t{credits} credits')


print()

# Not all escape characters are converted to a printed character.
print('123\b456')  # What does this print? What's missing?

