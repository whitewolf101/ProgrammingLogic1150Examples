""" Using regular expressions to decide if a string is in a correct
pattern.  In this example, an order number must be 
the letter A, 5 numbers and two letters, for example
A12345FG
A99999TN

"""
import re   # The regular expression library


def is_order_number_valid(order_number):
    pattern_string = r'A\d{5}[a-zA-Z]{2}'  # Letter A, 5 digits, two letters A-Z in any case
    pattern = re.compile(pattern_string)
    match = pattern.fullmatch(order_number)
    return match


def main():
    order_number = input('Enter the order number (A1111AA format): ')
    if is_order_number_valid(order_number):
        print(f'Thanks, {order_number} is a valid order number.')
    else:
        print('This is not a valid order number.')


main()
