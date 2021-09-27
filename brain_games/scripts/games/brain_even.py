#!/usr/bin/env python3
import random
from brain_games.scripts.game_engine import welcome_user, game


def is_even(num):
    if num % 2 == 0:
        return 'yes'
    return 'no'


def even_question_answer():
    result = []
    num = random.randint(1, 100)
    result.append(num)
    result.append(is_even(num))
    return result


def main():
    rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    name = welcome_user()
    game(name, rule, even_question_answer)


if __name__ == '__main__':
    main()
