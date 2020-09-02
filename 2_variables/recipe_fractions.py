# Recipe Calculator

# grilled cheese sandwiches

from fractions import Fraction  # include the Fraction library

# quantity for one serving, one sandwich, of each ingredient
slices_of_bread = 2
slices_of_cheese = 1
tablespoons_of_butter = Fraction(1, 4)   # this creates the fraction 1/4.
# The first number is the numerator, the number above the line,
# second is the denominator, the number below the line
# So if you wanted to make the fraction 3/5 for another ingredient, you would write
# teaspoons_of_mustard = Fraction(3, 5)

people = int(input('how many people want sandwiches? '))

# multiply ingredient by number of people to get total amount of each
bread = slices_of_bread * people
cheese = slices_of_cheese * people
butter = tablespoons_of_butter * people

# print recipe - can you  butter?
print('You need ' + str(bread) + ' slices of bread and '
      + str(cheese) + ' slices of cheese and ' + str(butter) + ' tablespoons of butter')

