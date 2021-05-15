#!/usr/bin/env python
from brain_games import cli

TEXT_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
STEPS = 3


def check_answer(answer, num):
    return is_even(num) and answer == 'yes' or not is_even(num) and answer == 'no'


def is_even(num):
    return num % 2 == 0


def play_game():
    count = 0
    while count < STEPS:
        random_num = cli.get_random_int(0, 10)
        answer = cli.get_user_answer(random_num)
        if check_answer(answer, random_num):
            count += 1
            print('Correct!')
        else:
            count = 10
            correct_answer = 'yes' if is_even(random_num) else 'no'
            cli.print_lose(answer, correct_answer)

    if count == 3:
        cli.print_win()


def main():
    cli.welcome_user()
    cli.print_desription(TEXT_DESCRIPTION)
    play_game()


if __name__ == '__main__':
    main()
