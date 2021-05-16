from brain_games import core
from random import randint
from math import sqrt
from itertools import count, islice


GAME_DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))


def get_question():
    return randint(1, 100)


def get_correct_answer(num):
    return 'yes' if is_prime(num) else 'no'


def run_game():
    core.start(get_question, get_correct_answer, GAME_DESCRIPTION)
