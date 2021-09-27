#!/usr/bin/env python3
import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def game(name_user, rule, questions_answers):
    print(rule)
    for i in range(3):
        result = questions_answers()
        question = result[0]
        answer = result[1]
        answer_user = prompt.string(f'Question: {question}\nYour answer: ')  # noqa: <error code>
        if answer_user == answer:
            print('Correct!')
        else:
            print(f"'{answer_user}' is wrong answer ;(. Correct answer was '{answer}'")  # noqa: <error code>
            print(f"Let's try again, {name_user}!")
            break
        if i == 2:
            print(f'Congratulations, {name_user}!')
