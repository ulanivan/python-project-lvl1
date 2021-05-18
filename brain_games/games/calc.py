from brain_games import core
from random import randint


DESCRIPTION = 'What is the result of the expression?'
OPERATORS = "+-*"


def get_random_sym():
    return OPERATORS[randint(0, len(OPERATORS) - 1)]


def get_question():
    random_sym = " {} ".format(get_random_sym())
    return str(randint(0, 100)) + random_sym + str(randint(0, 100))


def get_correct_answer(question):
    return str(eval(question))


def run_game():
    core.start(get_question, get_correct_answer, DESCRIPTION)
