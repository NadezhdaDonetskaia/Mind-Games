#!/usr/bin/env python3
import random


rule = 'What number is missing in the progression?'


def get_progression(first_num, len_prog, step):
    return [x for x in range(first_num, first_num + len_prog * step, step)]


def get_missing_num(progr):
    ind = random.randint(0, len(progr) - 1)
    return str(progr[ind])


def get_progression_without_num(progr, num):
    return ' '.join([str(x) if x != int(num) else '..' for x in progr])


def get_progression_question_answer():
    first_num = random.randint(1, 20)
    len_progr = random.randint(5, 15)
    step = random.randint(2, 15)
    progr = get_progression(first_num, len_progr, step)
    miss_num = get_missing_num(progr)
    question = get_progression_without_num(progr, miss_num)
    answer = miss_num
    return (question, answer)
