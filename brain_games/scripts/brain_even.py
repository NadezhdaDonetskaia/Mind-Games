import random
import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def even_num(name_user):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        num = random.randint(0, 100)
        if num % 2 == 0:
            answer_right = 'yes'
        else:
            answer_right = 'no'
        answer_user = prompt.string(f'Question: {num}\nYour answer: ')
        if answer_user == answer_right:
            print('Correct!')
        else:
            print(f"'{answer_user}' is wrong answer ;(. Correct answer was '{answer_right}'")
            print(f"Let's try again, {name_user}!")
            break
        if i == 2:
            print(f'Congratulations, {name_user}!')


def main():
    name = welcome_user()
    even_num(name)


if __name__ == '__main__':
    main()
    