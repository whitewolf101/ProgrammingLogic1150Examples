"""
Checking if a string is a valid ITEC class code using
regular expression - looking for the correct pattern of
ITEC plus a space plus 4 digits
"""

import re  # import the regular expression library

itec_class_code_pattern = r'ITEC \d{4}'  # Match a string with ITEC, space, and \d means any digit, {4} means \d repeated 4 times

test_string = 'ITEC 9999'  # Try changing this to other strings - what does the program print?

if re.fullmatch(itec_class_code_pattern, test_string):
    print(f'{test_string} is a valid class identifier')
else:
    print(f'{test_string} is NOT a valid class identifier')
