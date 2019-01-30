""" Changing a list item """

quiz_scores = [8, 4, 10, 9, 7]

# What if the user re-took the second quiz?
# Ask the user what their new score is

score = int(input('What is your score on the second quiz? '))

quiz_scores[1] = score
print(quiz_scores)   # What is quiz_scores now?

