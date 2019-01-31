
colleges = {'Minneapolis College': '1501 Hennepin Avenue, Minneapolis',
            'Metro State': '100 E 7th St, St. Paul',
            'Saint Paul College': '235 Marshall Avenue, St. Paul',
            'North Hennepin Community College': '7411 85th Ave N, Brooklyn Park',
            'Century College': '3300 Century Avenue N, White Bear Lake'}

for college in colleges:
    print(college)

# remove key-value pair with pop
colleges.pop('Metro State')
print(colleges)  # Everything except Metro State's key-value pair

# Like lists, pop will return the value for the key
century_address = colleges.pop('Century College')
print(century_address)  # 3300 Century Avenue N, White Bear Lake
print(colleges)   # key-value pair for Century College is removed

# Unlike lists, pop with no arguments does not work.
# You need to specify the key of the key-value pair to remove.
# Dictionaries don't have a concept of a last item

# colleges.pop()  # errors

# And if you try to delete a key that is not in the dictionary, it will error
# colleges.pop('Normandale Community College')  # Error - this key is not in the dictionary

# To clear all the data,
colleges.clear()
print(colleges)  # {}
