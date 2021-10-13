#!/usr/bin/env python3
import random

RULE = 'What is the result of the expression?'
# диапозон чисел для математических действий
FROM_NUM = 1
TO_NUM = 1000


def get_answer(num1, num2, operator):
    if operator == '+':
        return str(num1 + num2)
    elif operator == '-':
        return str(num1 - num2)
    else:
        return str(num1 * num2)


def get_calc_question_answer():
    operators = random.choice(['+', '-', '*'])
    num1 = random.randint(FROM_NUM, TO_NUM)
    num2 = random.randint(FROM_NUM, TO_NUM)
    question = f'{num1} {operators} {num2}'
    answer = get_answer(num1, num2, operators)
    return question, answer
