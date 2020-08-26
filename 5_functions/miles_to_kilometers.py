""" A program that converts miles to kilometers """


def main():
    miles = float(input('Please enter a number of miles'))
    kilometers = miles_to_kilometers(miles)
    print(f'{miles} miles is equal to {kilometers} kilometers.')


def miles_to_kilometers(miles):
    km = miles * 1.60934
    return km


main()
