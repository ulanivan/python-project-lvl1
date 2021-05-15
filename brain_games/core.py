import prompt

LAST_STEP = 3
EXIT_GAME = 10


def start(get_question, get_correct_answer, description):
    count = 0

    print("Welcome to the Brain Games!")
    print(description)
    user_name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(user_name))

    while count < LAST_STEP:
        question = get_question()
        correct_answer = get_correct_answer(question)
        answer = prompt.string("Question: {}\nYour answer: ".format(question))
        if answer == correct_answer:
            count += 1
            print("Correct!")
        else:
            count = EXIT_GAME
            print("'{}'is wrong answer ;(. \
                    Correct answer was '{}'. Let's try again, {}!".format(answer, correct_answer, user_name))

    if count == LAST_STEP:
        print("Congratulations, {}!".format(user_name))
