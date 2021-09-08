#!/usr/bin/env python3
import random
from brain_games.scripts.game_engine import welcome_user, game


def progression(first_num, len_prog, step):
    return [x for x in range(first_num, first_num + len_prog * step, step)]


def missing_num(progr):
    ind = random.randint(0, len(progr) - 1)
    return str(progr[ind])


def progression_without_num(progr, num):
    return ' '.join([str(x) if x != int(num) else '..' for x in progr])


def questions_answers():
    result = []
    for i in range(3):
        first_num = random.randint(1, 20)
        len_progr = random.randint(5, 15)
        step = random.randint(2, 15)
        progr = progression(first_num, len_progr, step)
        miss_num = missing_num(progr)
        result.append((progression_without_num(progr, miss_num), miss_num))  # noqa: <error code>
    return result


def main():
    rule = 'What number is missing in the progression?'
    name = welcome_user()
    game(name, rule, questions_answers())


if __name__ == '__main__':
    main()
