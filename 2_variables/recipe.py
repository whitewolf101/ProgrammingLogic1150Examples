# Recipe Calculator - multiplying quantities of ingredients for many people

# grilled cheese sandwiches

# quantity for one serving, one sandwich, of each ingredient
slices_of_bread = 2
slices_of_cheese = 1
tablespoons_of_butter = 1/4   # 0.25  Extra question - figure total for this?

# how many people? We could save a number in a variable...
# people = 3  # can you modify this number to use input?

# But it would be better to ask for the number of people
# question - what does this do without the int() part?
people = int(input('how many people want sandwiches? '))

# multiply ingredient by number of people to get total amount of each
bread = slices_of_bread * people
cheese = slices_of_cheese * people
butter = tablespoons_of_butter * people

# print recipe - can you include butter?
print('You need ' + str(bread) + ' slices of bread and ' + str(cheese) + ' slices of cheese and ' + str(butter) + ' tablespoons of butter')

