#!/usr/bin/env python3
import random


rule = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    if num % 2 == 0:
        return True
    return False


def get_even_question_answer():
    num = random.randint(1, 100)
    question = num
    if is_even(num):
        answer = 'yes'
    else:
        answer = 'no'
    return (question, answer)
