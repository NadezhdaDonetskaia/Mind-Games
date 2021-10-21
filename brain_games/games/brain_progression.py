#!/usr/bin/env python3
import random


RULE = 'What number is missing in the progression?'
# первое число в прогрессии от 1 до 20
MIN_FIRST_NUM = 1
MAX_FIRST_NUM = 20
# количество элементов прогрессии от 5 до 15
MIN_NUM_OF_EL = 5
MAX_NUM_OF_EL = 15
# общая разность варьируетсяот  2 до 15
MIN_COMMON_DIFF = 2
MAX_COMMON_DIFF = 15


def get_progression(first_num, num_of_el, common_diff):
    return [x for x in range(
        first_num, first_num + num_of_el * common_diff, common_diff)]


def get_missing_num(progression):
    ind = random.randint(0, len(progression) - 1)
    return progression[ind]


def get_progression_without_num(progression, num):
    # в данной конкретной задаче числа не повторяются, поэтому думаю,
    # что данное решение всё же имеет место быть:
    # return ' '.join([str(x) if x != num else '..' for x in progression])
    # но раз преподаватель сделал замечание, что лучше искать число по индексу,
    # то решение ниже, хоть и не проще
    ind = progression.index(num)
    return ' '.join([str(progression[x]) if x != ind else '..'
                     for x in range(len(progression))])


def get_progression_question_answer():
    first_num = random.randint(MIN_FIRST_NUM, MAX_FIRST_NUM)
    num_of_el = random.randint(MIN_NUM_OF_EL, MAX_NUM_OF_EL)
    common_diff = random.randint(MIN_COMMON_DIFF, MAX_COMMON_DIFF)
    progression = get_progression(first_num, num_of_el, common_diff)
    miss_num = get_missing_num(progression)
    question = get_progression_without_num(progression, miss_num)
    answer = str(miss_num)
    return question, answer
