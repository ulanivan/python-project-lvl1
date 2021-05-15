import prompt
from random import randint


def welcome_user():
    print("Welcome to the Brain Games!")
    global name
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))


def print_desription(text):
    print(text)


def get_random_int(start, end):
    return randint(start, end)


def get_user_answer(question):
    answer = prompt.string("Question: {}\nYour answer: ".format(question))
    return answer


def print_win():
    print("Congratulations, {}!".format(name))


def print_lose(wrong_asnwer, correct):
    print("'{}' is wrong answer ;(. Correct answer was '{}'. Let's try again, {}!".format(wrong_asnwer, correct, name))
