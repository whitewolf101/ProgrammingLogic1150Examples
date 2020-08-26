""" Using a function to determine if a temperature is above freezing
Calling the function multiple times in the program """


def above_freezing(temp):
    if temp > 32:
        return 'above freezing'
    else:
        return 'below freezing'


def main():

    # Call the above_freezing function, in different ways

    today_temp = float(input('Please enter today\'s high temperature: '))
    # Save the result of the function call, then use it in a print statement
    print('It will be ' + above_freezing(today_temp) + ' today')

    tonight_temp = float(input('Please enter tonight\'s low temperature: '))
    # Calling the function, saving the return value in a new variable, using
    # it later in the program in the print statement
    above_below_tonight = above_freezing(tonight_temp)
    print('It will be ' + above_below_tonight + ' tonight')

    tomorrow_temp = float(input('Please enter tomorrows\'s high temperature: '))
    # Calling the function in a f-string
    print(f'It will be {above_freezing(tomorrow_temp)} tomorrow')


main()
