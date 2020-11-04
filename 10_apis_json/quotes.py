""" Random quote and author from the Quote Garden API
API documentation: https://pprathameshmore.github.io/QuoteGarden/#get-a-random-quote
Try running the program several times and verify a new quote is returned each time
"""

import requests

# random quote request URL - expect a response in JSON (pronounced "jason") form
url = 'https://quote-garden.herokuapp.com/api/v2/quotes/random'

response = requests.get(url).json()   # response is a dictionary with a nested dictionary

# print(response)  # optional - to help see what the data you are working with is

# Extract data that we need
quote_data = response['quote']   # this is also a dictionary

# print(quote_data)   # optional - to help see what the data you are working with is

# Get the quoteText, and just print that
quote_text = quote_data['quoteText']   # get the text - use the exact text of the key
quote_author = quote_data['quoteAuthor']  # and the author too

# Use data in our program
print(f'A random quote is:')
print(quote_text)
print(f'By: {quote_author}')
