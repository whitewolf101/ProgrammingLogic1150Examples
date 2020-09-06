"""
Checking if a string is a valid ITEC class code
"""

test_string = 'ITEC 1150'  # Try changing this to other strings - what does the program print?


if len(test_string) == 9 and test_string.upper().startswith('ITEC'):
    print(f'{test_string} is a valid class identifier')
else:
    print(f'{test_string} is NOT a valid class identifier')
