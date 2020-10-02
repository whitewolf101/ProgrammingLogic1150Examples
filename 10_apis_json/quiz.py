import requests

""" Quiz program using questions from the Open Trivia Database 
https://opentdb.com/
"""

def main():
    number_of_questions = 10
    url = f'https://opentdb.com/api.php?amount={number_of_questions}&type=boolean'

    questions_response = requests.get(url).json()

    questions = questions_response['results']

    correct_answers = 0

    for question in questions:
        user_answered_correctly = ask_question(question)
        if user_answered_correctly:
            correct_answers += 1

    print(f'You answered {correct_answers} question(s) correctly out of {number_of_questions}.')


def ask_question(question_dictionary):
    question = question_dictionary['question']
    category = question_dictionary['category']
    difficulty = question_dictionary['difficulty']

    correct_answer = question_dictionary['correct_answer']

    print(f'This is a {difficulty} question in the category {category}. Enter "True" or "False".')

    answer = input(question + ' ').title()
    while answer not in ['True', 'False']:
        print('Please Enter "True" or "False".')
        answer = input(question + ' ').title()

    if answer == correct_answer:
        print('Correct!')
        return True   # the user got the answer correct
    else:
        print(f'Sorry, the answer is {correct_answer}')
        return False   # the user got the answer wrong


main()