""" Changing a list item, modifying index to be more human-friendly """

quiz_scores = [8, 4, 10, 9, 7]

# What if the user re-took any one of the quizzes?
# Ask the user what quiz they re-took
# For this program, the user has to enter 1 for the first quiz,
# 2 for the second quiz ... more human-friendly
quiz = int(input('Which quiz did you re-take? '))

# Ask the user what their new score is
score = int(input(f'What is your score on quiz {quiz}? '))

quiz_scores[quiz - 1] = score
print(quiz_scores)   # What is quiz_scores now?


