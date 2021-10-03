#!/usr/bin/env python3
import random


rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_is_prime(num):
    prime_nums = [2]
    counter = 3
    while counter <= num:
        for n in prime_nums:
            if num % n == 0:
                counter = num + 1
                break
            if counter == num:
                return 'yes'
        prime_nums.append(counter)
        counter += 1
    if num in prime_nums:
        return 'yes'
    return 'no'


def get_prime_question_answer():
    num = random.randint(1, 1000)
    question = num
    answer = get_is_prime(num)
    return (question, answer)
