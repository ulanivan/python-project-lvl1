from brain_games import core
from random import randint
import math


GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question():
    return "{} {}".format(randint(0, 100), randint(0, 100))


def get_correct_answer(question):
    first_num, second_num = question.split(" ")
    return str(math.gcd(int(first_num), int(second_num)))


def run_game():
    core.start(get_question, get_correct_answer, GAME_DESCRIPTION)
