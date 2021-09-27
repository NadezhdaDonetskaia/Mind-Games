#!/usr/bin/env python3
import random
from brain_games.scripts.game_engine import welcome_user, game


def calc(num1, num2, operator):
    if operator == '+':
        return str(num1 + num2)
    elif operator == '-':
        return str(num1 - num2)
    else:
        return str(num1 * num2)


def calc_question_answer():
    result = []
    operators = random.choice(['+', '-', '*'])
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    result.append(f'{num1} {operators} {num2}')
    result.append(calc(num1, num2, operators))
    return result


def main():
    rule = 'What is the result of the expression?'
    name = welcome_user()
    game(name, rule, calc_question_answer)


if __name__ == '__main__':
    main()
