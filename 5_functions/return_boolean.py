"""
A function can return any type of value needed to represent the result.
So, a function can return one of the boolean values True or False.
"""


def main():

    print('Should you wear a hat today? Please tell me the weather')
    temp = float(input('What is the temperature, in Fahrenheit? '))
    snow\
        = input('Is it snowing? Enter "Y" for yes, anything else for no: ')

    need_hat = should_wear_hat(temp, snow)

    if need_hat:
        print('You should wear a hat')
    else:
        print('It is not too cold and not snowing.')


def should_wear_hat(temp, snow):
    if temp < 40 or snow.lower() == 'y':
        return True
    else:
        return False


main()
