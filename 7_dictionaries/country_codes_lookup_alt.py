""" Country code lookup using in """


# Dictionary of country codes and full names
country_codes = {
    'CN': 'China',
    'FR': 'France',
    'MX': 'Mexico',
}

code = input('Enter the country code to look up: ')

# Check to see if code is in dictionary
if code in country_codes:
    # If the code is in the dictionary, can read without worrying about key errors
    country = country_codes[code]
    print(f'The country for {code} is {country}')
else:
    # Print not found message
    print(f'Country for code {code} not found.')

