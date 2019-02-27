""" Sorting a list. Lists of strings are sorted alphabetically.
 Lists of numbers are sorted from smallest to largest. """

colleges = ['Minneapolis College',
            'Metro State',
            'Saint Paul College',
            'North Hennepin Community College',
            'Century College']

colleges.sort()  # Rearranges the list into alphabetical order

for college in colleges:
    print(college)


credits_per_class = [4, 2, 5, 1]

credits_per_class.sort()

print(credits_per_class)  # [1, 2, 4, 5]

