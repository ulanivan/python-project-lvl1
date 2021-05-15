from brain_games import core
from random import randint


GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def get_question():
    return randint(0, 100)


def get_correct_answer(num):
    return 'yes' if is_even(num) else 'no'


def run_game():
    core.start(get_question, get_correct_answer, GAME_DESCRIPTION)
