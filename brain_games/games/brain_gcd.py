#!/usr/bin/env python3
import random


RULE = 'Find the greatest common divisor of given numbers.'
# диапозон чисел, среди которых будем искать наибольший общий делитель
FROM_NUM = 1
TO_NUM = 1000


def get_gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return num1 + num2


def get_gcd_question_answer():
    num1 = random.randint(FROM_NUM, TO_NUM)
    num2 = random.randint(FROM_NUM, TO_NUM)
    question = f'{num1} {num2}'
    answer = str(get_gcd(num1, num2))
    return question, answer
