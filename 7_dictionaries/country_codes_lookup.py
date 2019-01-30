
# Dictionary of country codes and full names
country_codes = {
    'CN': 'China',
    'FR': 'France',
    'MX': 'Mexico',
}

code = input('Enter the country code to look up: ')

# Read code from dictionary.
# get() returns the value if the key is found
# get() returns None if they key is not found.
# Check if a code was returned, or None.
# In Python, None is considered to be false. Any non-empty string is True.

country = country_codes.get(code)  # country will be None if code is not in dictionary
if country:
    print(f'The country for {code} is {country}')
else:
    print(f'Country for code {code} not found.')

