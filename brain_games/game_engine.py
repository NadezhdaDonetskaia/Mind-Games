#!/usr/bin/env python3
import prompt

def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def start_game(rule, questions_answers):
    user_name = welcome_user()
    print(rule)
    for i in range(3):
        question, answer = questions_answers()
        answer_user = prompt.string(f'Question: {question}\n'
                                    f'Your answer: ')
        if answer_user == answer:
            print('Correct!')
        else:
            print(f"'{answer_user}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'")
            print(f"Let's try again, {user_name}!")
            break
        if i == 2:
            print(f'Congratulations, {user_name}!')



