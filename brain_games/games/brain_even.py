#!/usr/bin/env python3
import random


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
# диапозон числа, среди которых будем проверять на четность и нечетность
FROM_NUM = 1
TO_NUM = 1000


def is_even(num):
    return num % 2 == 0


def get_even_question_answer():
    num = random.randint(FROM_NUM, TO_NUM)
    question = num
    answer = 'yes' if is_even(num) else 'no'
    return question, answer
