#!/usr/bin/env python3
import random


rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# функция нужна для реализации «Решета Эратосфена»
def is_in_prime_list(num, prime_list):
    for el in prime_list:
        if num % el == 0:
            return False
    return True


def is_prime(num):
    prime_nums = [2]
    """
    собираем все простые числа до нашего числа
    """
    for i in range(3, num + 1):
        if is_in_prime_list(i, prime_nums):
            prime_nums.append(i)
    return num in prime_nums


def get_prime_question_answer():
    num = random.randint(1, 1000)
    question = num
    if is_prime(num):
        answer = 'yes'
    else:
        answer = 'no'
    return (question, answer)
