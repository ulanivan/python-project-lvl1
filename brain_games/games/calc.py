from brain_games import core
from random import randint


GAME_DESCRIPTION = 'What is the result of the expression?'
OPERATORS = "+-*"


def get_random_sym():
    return OPERATORS[randint(0, len(OPERATORS) - 1)]


def get_question():
    return str(randint(0, 10)) + " {} ".format(get_random_sym()) + str(randint(0, 10))


def get_correct_answer(question):
    return str(eval(question))


def run_game():
    core.start(get_question, get_correct_answer, GAME_DESCRIPTION)
