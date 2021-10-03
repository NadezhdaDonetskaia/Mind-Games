#!/usr/bin/env python3
import random

rule = 'What is the result of the expression?'


def get_calc(num1, num2, operator):
    if operator == '+':
        return str(num1 + num2)
    elif operator == '-':
        return str(num1 - num2)
    else:
        return str(num1 * num2)


def get_calc_question_answer():
    operators = random.choice(['+', '-', '*'])
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f'{num1} {operators} {num2}'
    answer = get_calc(num1, num2, operators)
    return (question, answer)
