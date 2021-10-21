#!/usr/bin/env python3
import prompt


NUM_OF_ROUNDS = 3


def run_game(rule, get_questions_answers):
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(rule)
    for i in range(NUM_OF_ROUNDS):
        question, answer = get_questions_answers()
        answer_user = prompt.string(f'Question: {question}\n'
                                    f'Your answer: ')
        if answer_user == answer:
            print('Correct!')
        else:
            print(f"'{answer_user}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'")
            print(f"Let's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')
