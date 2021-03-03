"""
A multiple-choice quiz.

An example question,

What component in a computer stores data persistently?
1: Memory
2: Hard drive
3: CPU
4: Monitor

How would we store the answers and the correct answer?

"""

import random


def main():
    question = 'What component in a computer stores data persistently?'
    answers = ['Hard drive', 'CPU', 'Memory', 'Monitor']   # Create list of answers with the right answer first
    ask_question(question, answers)

    question = 'Who is one of the founders of Microsoft?'
    answers = ['Bill Gates', 'Elon Musk', 'Larry Ellison', 'Steve Jobs']   # Correct answer first
    ask_question(question, answers)


def ask_question(question, answers):
    # The correct answer is the first answer in the answers list
    correct_answer = answers[0]
    random.shuffle(answers)

    print()  # blank line

    print(question)

    for index, answer in enumerate(answers):
        print(f'{index}: {answer}')

    user_answer_number = int(input('Enter the number for your answer: '))

    # check that the choice is a number between 0 and the maximum list index
    while user_answer_number < 0 or user_answer_number > len(answers) - 1:
        user_answer_number = int(input('Not a valid choice, Enter the number for your answer: '))

    if answers[user_answer_number] == correct_answer:
        print('Correct!')
    else:
        print(f'Sorry, the correct answer is {correct_answer}')

    print()  # blank line


main()

