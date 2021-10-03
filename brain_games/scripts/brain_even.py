#!/usr/bin/env python3
from brain_games.games.brain_even import rule, get_even_question_answer
from brain_games.game_engine import start_game


def main():
    start_game(rule, get_even_question_answer)


if __name__ == '__main__':
    main()
