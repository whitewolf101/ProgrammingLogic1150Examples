from urllib import request
import json

"""
Complete this program that calculates conversions between US dollars and other currencies.

In your main function, start a loop.
In the loop, ask the user what currency code they would like to convert to
And, how many dollars they want to convert.

Call the get_exchange_rates() function. 
This function returns a dictionary with another dictionary inside it. 
You'll need to get the exchange rate from the dictionary.

Then, do the math. For example, if the user wants to convert $100 to Euros (EUR), 
and the exchange rate is 0.874, then you need to multiply the US Dollar amount by 
the exchange rate to get the amount in Euros. $100 is about $87 Euro.

Don't modify the get_exchange_rates function or the example_exchange_rates function. 

"""


def main():
    print('Write your code here.')




# You do not need to modify any code below this line.
def get_exchange_rates():

    url = 'https://api.exchangeratesapi.io/latest?base=USD'

    try:
        response = request.urlopen(url).read()
        data = json.loads(response)
        return data
    except:
        print('Error fetching data. Check that you are online? Using placeholder data.')
        return example_exchange_rates()


def example_exchange_rates():
    return {
       "base": "USD",
       "date": "2019-01-30",
       "rates": {
          "ISK": 119.8705048561,
          "CAD": 1.3221629189,
          "MXN": 19.0960713973,
          "CHF": 0.9977250853,
          "AUD": 1.3898853793,
          "CNY": 6.7168606177,
          "GBP": 0.7642050923,
          "USD": 1.0,
          "SEK": 9.0859217779,
          "NOK": 8.4817569341,
          "TRY": 5.2750021874,
          "IDR": 14130.0026249016,
          "ZAR": 13.6043398373,
          "HRK": 6.4953189255,
          "EUR": 0.8749671887,
          "HKD": 7.8451308076,
          "ILS": 3.6677749584,
          "NZD": 1.4632076297,
          "MYR": 4.1057835331,
          "JPY": 109.4408959664,
          "CZK": 22.5759034036,
          "SGD": 1.3510368361,
          "RUB": 65.9388397935,
          "RON": 4.1605564791,
          "HUF": 276.9533642488,
          "BGN": 1.7112608277,
          "INR": 71.1794557704,
          "KRW": 1118.1905678537,
          "DKK": 6.5314550704,
          "THB": 31.3798232566,
          "PHP": 52.3002887392,
          "PLN": 3.7540467232,
          "BRL": 3.7091609065
       }
    }

main()