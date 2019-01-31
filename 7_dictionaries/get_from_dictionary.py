
colleges = {'Minneapolis College': '1501 Hennepin Avenue, Minneapolis',
            'Metro State': '100 E 7th St, St. Paul',
            'Saint Paul College': '235 Marshall Avenue, St. Paul',
            'North Hennepin Community College': '7411 85th Ave N, Brooklyn Park',
            'Century College': '3300 Century Avenue N, White Bear Lake'}

# Use the [] notation to read a value for a key
metro_state_address = colleges['Metro State']
print(metro_state_address)  # 100 E 7th St, St. Paul
# The dictionary is not modified
print(colleges)

# The [] method will error if the key is not found
# normandale_address = colleges['Normandale Community College']  # Key error

# If you are not sure a key is in the dictionary, use get() method
# Again, the dictionary will not be modified
normandale_address = colleges.get('Normandale Community College')  # Returns None
print(normandale_address)  # None
metro_state_address = colleges.get('Metro State')  # Returns '100 E 7th St, St. Paul'
print(metro_state_address)  # '100 E 7th St, St. Paul'


