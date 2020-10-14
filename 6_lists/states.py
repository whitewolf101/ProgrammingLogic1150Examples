state_names = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]

# how many states and territories?
number_of_states_and_territories = len(state_names)
print(number_of_states_and_territories)

# Ask user for their state
user_state = input('What state to deliver to? ')  # this is a delivery program

# is it in the state_names list?
if user_state.title() in state_names:  # ok solution... not perfect.
    print('Thanks - we recognize your state')
else:
    print('That state is not recognized')

# another solution .... more general solution. how do we tell the user it's not recognized?
found = False  # boolean variable - assume the state is not found
for state in state_names:
    if user_state.lower() == state.lower():
        print('Thanks - we recognize your state')  # unless it is!
        found = True  # set the boolean variable to be true. It will only be true if the condition is true

if not found:
    print('Your state is not found')
else:
    print('just to confirm, we recognize your state')  # printing message in the loop, but could do it here too

# extra questions

# 1. Can you write a validation while loop so user can try again if state is invalid? Would a function help?

# 2. Can you make a new list with only states that have a letter or set
# of letters in? Be case-insensitive. So 'ca' matches California, American Samoa, North Carolina, South Carolina

search_letters = 'ca'
# make list of California, American Samoa, North Carolina, South Carolina
matching_states = []
# tip - use a loop, and append matches to matching_states

# tip: we can use the in operator with strings too
# if 'python' in 'this class uses the python programming language':
#     print('found it!')
