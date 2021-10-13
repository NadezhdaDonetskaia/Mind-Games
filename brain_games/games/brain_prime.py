#!/usr/bin/env python3
import random


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
# диапозон числа, среди которых будем проверять на простое
FROM_NUM = 1
TO_NUM = 1000


def is_prime(num):
    if num < 2:
        return False
    answer = True
    for i in range(2, num):
        if num % i == 0:
            answer = False
            break
    return answer


def get_prime_question_answer():
    num = random.randint(FROM_NUM, TO_NUM)
    question = num
    if is_prime(num):
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
