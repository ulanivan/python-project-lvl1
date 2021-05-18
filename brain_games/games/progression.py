from brain_games import core
from random import randint


GAME_DESCRIPTION = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 12


def get_question():
    first_num = randint(0, 10)
    diff = randint(1, 5)
    element_index = randint(1, PROGRESSION_LENGTH - 1)
    result = ""
    for i in range(PROGRESSION_LENGTH):
        if element_index == i:
            result += ".. "
        else:
            result += "{} ".format(str(first_num + diff * i))
    return result


def get_correct_answer(question):
    elems = question.split(" ")
    first = int(elems[0])
    second = int(elems[1])
    diff = second - first
    elem_index = elems.index("..")
    return str(first + diff * elem_index)


def run_game():
    core.start(get_question, get_correct_answer, GAME_DESCRIPTION)
