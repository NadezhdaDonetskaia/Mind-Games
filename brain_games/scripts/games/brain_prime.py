#!/usr/bin/env python3
import random
from brain_games.scripts.game_engine import welcome_user, game


def is_simple(num, my_list):
    for i in range(len(my_list)):
        if num % my_list[i] == 0:
            return False
    return True


def my_simple(num):
    simple_nums = [2, 3]
    if num in simple_nums:
        return 'yes'
    counter = 4
    while counter <= num:
        if is_simple(counter, simple_nums):
            if counter == num:
                return 'yes'
            simple_nums.append(counter)
        counter += 1
    return 'no'


def questions_answers():
    result = []
    for i in range(3):
        num = random.randint(1, 1000)
        result.append((num, my_simple(num)))
    return result


def main():
    rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    name = welcome_user()
    game(name, rule, questions_answers())


if __name__ == '__main__':
    main()
