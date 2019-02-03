""" Alignment operators < > ^ in format strings
Padding with other characters
"""


message = "Hello"
print(f'{message:20}')    # left aligned - default for string with no alignment operator
print(f'{message:<20}')   # left aligned
print(f'{message:>20}')   # Right aligned in a 20-character area
print(f'{message:^20}')   # Centered in a 20-character area

print()

number = 42
print(f'{number:20}')     # right aligned - default for numbers with no alignment operator
print(f'{number:<20}')    # left aligned
print(f'{number:>20}')    # Right aligned in a 20-character area
print(f'{number:^20}')    # Centered in a 20-character area

print()

total = 123.456
print(f'{total:20}')     # right aligned - default for numbers with no alignment operator
print(f'{total:<20}')    # left aligned
print(f'{total:>20}')    # Right aligned in a 20-character area
print(f'{total:^20}')    # Centered in a 20-character area

print()

print(f'{message:o<20}')   # left aligned, padded with o
print(f'{message:o>20}')   # Right aligned in a 20-character area, padded with o
print(f'{message:o^20}')   # Centered in a 20-character area, padded with o

print()

print(f'{number:-<20}')    # left aligned, padded with -
print(f'{number:->20}')    # Right aligned in a 20-character area, padded with -
print(f'{number:-^20}')    # Centered in a 20-character area, padded with -

print()

print(f'{total:$<20}')    # left aligned, padded with $
print(f'{total:$>20}')    # Right aligned in a 20-character area, padded with $
print(f'{total:$^20}')    # Centered in a 20-character area, padded with $
