#!/usr/bin/env python3
import random


rule = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    if num % 2 == 0:
        return 'yes'
    return 'no'


def get_even_question_answer():
    num = random.randint(1, 100)
    question = num
    answer = is_even(num)
    return (question, answer)
