""" Using regular expressions to decide if a StarID is the right
pattern of letter letter number number number number letter letter """

import re   # The regular expression library


def is_star_id(star_id):
    pattern_string = '[a-z]{2}\d{4}[a-z]{2}'
    pattern = re.compile(pattern_string)
    match = pattern.match(star_id)
    return match


def main():
    star_id = input('Enter your star ID: ')
    if is_star_id(star_id):
        print('thanks, valid star ID')
    else:
        print('This is not a valid star ID.')


main()
