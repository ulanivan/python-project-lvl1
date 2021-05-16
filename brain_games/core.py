import prompt

LAST_STEP = 3
EXIT_GAME = 10
YOU_LOSE_STRING = "'{}' is wrong answer ;(. Correct answer was '{}'. Let's try again, {}!"


def start(get_question, get_correct_answer, description):
    count = 0

    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(user_name))
    print(description)

    while count < LAST_STEP:
        question = get_question()
        correct_answer = get_correct_answer(question)
        answer = prompt.string("Question: {}\nYour answer: ".format(question))
        if answer == correct_answer:
            count += 1
            print("Correct!")
        else:
            count = EXIT_GAME
            print(YOU_LOSE_STRING.format(answer, correct_answer, user_name))

    if count == LAST_STEP:
        print("Congratulations, {}!".format(user_name))
