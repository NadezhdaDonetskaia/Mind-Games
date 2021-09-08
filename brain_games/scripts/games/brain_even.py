#!/usr/bin/env python3
import random
from brain_games.scripts.game_engine import welcome_user, game


def is_even(num):
    if num % 2 == 0:
        return 'yes'
    return 'no'


def questions_answers():
    result = []
    for i in range(3):
        num = random.randint(1, 100)
        result.append((num, is_even(num)))
    return result


def main():
    rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    name = welcome_user()
    game(name, rule, questions_answers())


if __name__ == '__main__':
    main()