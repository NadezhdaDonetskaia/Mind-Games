#!/usr/bin/env python3
import random


rule = 'What number is missing in the progression?'
# первое число от 1 до 20
min_first_num = 1
max_first_num = 20
# количество элементов прогрессии от 5 до 15
min_num_of_el = 5
max_num_of_el = 15
# общая разность варьируетсяот  2 до 15
min_common_diff = 2
max_common_diff = 15


def get_progression(first_num, num_of_el, common_diff):
    return [x for x in range(
        first_num, first_num + num_of_el * common_diff, common_diff)]


def get_missing_num(progr):
    ind = random.randint(0, len(progr) - 1)
    return progr[ind]


def get_progression_without_num(progr, num):
    return ' '.join([str(x) if x != num else '..' for x in progr])


def get_progression_question_answer():
    first_num = random.randint(min_first_num, max_first_num)
    num_of_el = random.randint(min_num_of_el, max_num_of_el)
    common_diff = random.randint(min_common_diff, max_common_diff)
    progr = get_progression(first_num, num_of_el, common_diff)
    miss_num = get_missing_num(progr)
    question = get_progression_without_num(progr, miss_num)
    answer = str(miss_num)
    return (question, answer)
