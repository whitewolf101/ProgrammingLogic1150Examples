""" Reading data from the dictionary, checking if things are in the dictionary """


colleges = {'Minneapolis College': '1501 Hennepin Avenue, Minneapolis',
            'Metro State': '100 E 7th St, St. Paul',
            'Saint Paul College': '235 Marshall Avenue, St. Paul',
            'North Hennepin Community College': '7411 85th Ave N, Brooklyn Park',
            'Century College': '3300 Century Avenue N, White Bear Lake'}

for college in colleges:
    print(college)

# Two ways to check if a key is in a dictionary: in and get()

# Use in
# This is good if you only need to check if it's there
# in does not modify the dictionary

if 'Normandale Community College' in colleges:
    print('Normandale is in the dictionary')
else:
    print('Normandale is not in the dictionary')   # This is printed

if 'Minneapolis College' in colleges:
    print('Minneapolis College is in the dictionary')  # This is printed
else:
    print('Minneapolis College is not in the dictionary')


# Use get()
# This is good if you need to check and you need the value for the key
# get() does not modify the dictionary.

normandale_address = colleges.get('Normandale Community College')
if normandale_address:
    print(f'Normandale College\'s address is {normandale_address}')
else:
    print('Normandale College address not found.')  # This prints: Normandale College address not found.


minneapolis_address = colleges.get('Minneapolis College')
if minneapolis_address:
    print(f'Minneapolis College\'s address is {minneapolis_address}')  # This prints: Minneapolis College's address is 1501 Hennepin Avenue, Minneapolis
else:
    print('Minneapolis College address not found.')

