""" A function to decide if a class code is
first year, second year, or something else """


def first_year_second_year(class_code):

    # Return 'First year' for class codes between 1000-1999
    # Return 'Second year' for class codes between 2000-2999
    # Return 'Not first year or second year' for anything else

    if class_code >= 1000 and class_code <= 1999:
        return 'First year'
    elif class_code >= 2000 and class_code <= 2999:
        # print('2nd year') # what does this do? Why isn't this right?
        return 'Second year'
    else:
        return "Not first year or second year"


def main():
    print(first_year_second_year(1150))  # First year
    print(first_year_second_year(2560))  # Second year
    print(first_year_second_year(4000))  # Not first year or second year


main()
