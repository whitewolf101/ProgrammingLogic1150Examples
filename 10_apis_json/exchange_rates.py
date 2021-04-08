import requests

# The URL of the API server with exchange rate data
url = 'https://api.ratesapi.io/latest?base=USD&symbols=EUR'

dollars = float(input('Enter number of dollars to convert to Euros: '))

# Make request to API server, covert the json() response into a Python dictionary
response = requests.get(url).json()

# Get the value of the EUR key from the rates dictionary
exchange_rate = response['rates']['EUR']

# Math - multiply the number of dollars by the exchange rate to get the equivalent in Euros
euros = dollars * exchange_rate

# Display result, using string formatting to round Euro amount to 2 decimal places
print(f'${dollars} is equivalent to {euros:.2f} Euros. ')

