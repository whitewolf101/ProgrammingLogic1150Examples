""" Using the in operator to see if an element is in a list """

villains = ['Catwoman', 'Darth Vader', 'Sauron', 'Lex Luthor', 'Magneto']
if 'Darth Vader' in villains:
    print('Darth Vader is in the list')
else:
    print('Darth Vader is NOT in the list')

if 'Voldemort' in villains:
    print('Voldemort is in the list')
else:
    print('Voldemort is NOT in the list')


# Works with numbers too

class_codes = [1005, 1100, 1110, 1150, 1310, 1425]
if 1150 in class_codes:
    print('1150 Programming Logic is in the list of class codes')

