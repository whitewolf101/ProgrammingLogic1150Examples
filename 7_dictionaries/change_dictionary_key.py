
colleges = {'Minneapolis College': '1501 Hennepin Avenue, Minneapolis',
            'Metro State': '100 E 7th St, St. Paul',
            'Saint Paul College': '235 Marshall Avenue, St. Paul',
            'North Hennepin Community College': '7411 85th Ave N, Brooklyn Park',
            'Century College': '3300 Century Avenue N, White Bear Lake'}

for college in colleges:
    print(college)

# Metro State has another campus at Harmon Place
colleges['Metro State'] = 'Harmon Place, Minneapolis'

print(colleges)
# Metro State key's value has changed
# {'Minneapolis College': '1501 Hennepin Avenue, Minneapolis', 'Metro State': 'Harmon Place, Minneapolis', 'Saint Paul College': '235 Marshall Avenue, St. Paul', 'North Hennepin Community College': '7411 85th Ave N, Brooklyn Park', 'Century College': '3300 Century Avenue N, White Bear Lake'}

# If you try and change a key that doesn't exist, it will be added to the dictionary
colleges['Hennepin Technical College'] = '13100 College View Dr, Eden Prairie'
# This includes a new key: value for Hennepin Technical College
# {'Minneapolis College': '1501 Hennepin Avenue, Minneapolis', 'Metro State': 'Harmon Place, Minneapolis', 'Saint Paul College': '235 Marshall Avenue, St. Paul', 'North Hennepin Community College': '7411 85th Ave N, Brooklyn Park', 'Century College': '3300 Century Avenue N, White Bear Lake'}
