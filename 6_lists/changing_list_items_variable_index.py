""" Changing a list item with zero-based index """

quiz_scores = [8, 4, 10, 9, 7]

# What if the user re-took any one of the quizzes?
# Ask the user what quiz they re-took
# For this program, the user has to enter 0 for the first quiz,
# or 1 for the second quiz
quiz = int(input('Which quiz did you re-take? '))

# Ask the user what their new score is
score = int(input(f'What is your score on quiz {quiz}? '))

quiz_scores[quiz] = score
print(quiz_scores)   # What is quiz_scores now?

