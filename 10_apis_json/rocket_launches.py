""" List of upcoming rocket launches from the Space Devs Launch Library API
https://thespacedevs.com/
https://ll.thespacedevs.com/2.0.0/swagger

This API server appears to be a Python program too.
"""

import requests
from pprint import pprint  # pretty print - optional - makes it easier to see the structure of the response

url = 'https://ll.thespacedevs.com/2.0.0/launch/upcoming/?mode=list&limit=10'
response = requests.get(url).json()
# print(response)  # the JSON response, all on one line
# pprint(response)  # Alternative: extra p - pprint stands for "pretty print" - easier to read and see structure of response

# The response is a dictionary with a results key
# The results key's value is a list of launches
# Each launch is a dictionary
results_list = response['results']
# pprint(results_list)

# For each launch, get the location, name, and window_start - time they'll try and launch

for launch in results_list:  # launch is one dictionary for one launch
    # pprint(launch)
    name = launch['name']
    location = launch['location']
    window_start = launch['window_start']
    print(name)
    print(location)
    print(window_start)
    print()
