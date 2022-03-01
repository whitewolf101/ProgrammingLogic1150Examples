import random
import string

from words import word_list

GREEN = '\u001b[32;1m'
YELLOW = '\u001b[33;1m'
RESET = '\u001b[0m'

CORRECT_STATUS = "CORRECT"
CORRECT_LETTER_WRONG_PLACE_STATUS = "CORRECT WRONG PLACE"


def show_board(board, correct_answer):
    print()
    for line in board:
        show_line(line, correct_answer)
    print()


def pad(letter):
    return f' {letter} '


def show_line(line, correct_answer):

    print('|', end='')

    for guessed_letter, correct_letter in zip(line, correct_answer):
        letter = pad(guessed_letter)
        if guessed_letter == correct_letter:
            print(GREEN + letter + RESET, end='')
        elif guessed_letter in correct_answer:
            print(YELLOW + letter + RESET, end='')
        else:
            print(letter, end='')

        print('|', end='')

    print()


def choose_word():
    return random.choice(word_list)


def get_users_guess():
    while True:
        guess = input('Enter your guess: ').upper()
        if guess not in word_list:
            print('Not a valid word!')
        else:
            return guess


def update_board(board, current_line_index, guess):
    guess_as_list = list(guess)
    board[current_line_index] = guess_as_list


def show_guessed_letters(guessed_letters):

    print('Guessed so far: ', end='')

    for letter, status in guessed_letters.items():
        if status == CORRECT_STATUS:
            print(GREEN + letter + RESET, end='')
        elif status == CORRECT_LETTER_WRONG_PLACE_STATUS:
            print(YELLOW + letter + RESET, end='')
        else:
            print(letter, end='')
    print()


def update_guessed_letters(guessed_letters, guess, correct_answer):
    for guessed_letter, correct_answer_letter in zip(guess, correct_answer):
        if guessed_letter == correct_answer_letter:
            guessed_letters[guessed_letter] = CORRECT_STATUS
        elif guessed_letter in correct_answer and guessed_letters[guessed_letter] != "CORRECT":
            guessed_letters[guessed_letter] = CORRECT_LETTER_WRONG_PLACE_STATUS
        else:
            pass


def main():

    board = [
        [' '] * 5,
        [' '] * 5,
        [' '] * 5,
        [' '] * 5,
        [' '] * 5,
        [' '] * 5,
    ]

    guessed_letters = dict(zip(string.ascii_uppercase, [''] * 26))

    correct_answer = choose_word()
    print(correct_answer)
    for current_line_index in range(6):
        show_board(board, correct_answer)
        show_guessed_letters(guessed_letters)
        guess = get_users_guess()
        update_guessed_letters(guessed_letters, guess, correct_answer)
        update_board(board, current_line_index, guess)
        if guess == correct_answer:
            show_board(board, correct_answer)
            print(f"You won with {current_line_index + 1} attempts!")
            break
    else:
        print(f'Sorry, the answer is {correct_answer}')

main()
