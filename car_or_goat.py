#!/usr/bin/env python3

# https://en.wikipedia.org/wiki/Monty_Hall_problem

import random
import logging

CHOICES = [1, 2, 3]


def get_car_1():
    car = random.choice(CHOICES)

    # the player pick a door, and do not change
    guess = random.choice(CHOICES)

    return guess == car


def get_car_2():
    car = random.choice(CHOICES)

    # the player pick a door
    guess = random.choice(CHOICES)

    # the host open a door with a goat
    choices = CHOICES[:]
    choices.remove(car)
    if guess != car:
        choices.remove(guess)

    opened = random.choice(choices)

    # the player change his guess
    choices = CHOICES[:]
    choices.remove(opened)
    choices.remove(guess)
    guess = choices[0]

    return guess == car


def main():
    fmt = "%(asctime)s %(filename)s [%(lineno)d][%(levelname)s] %(message)s"
    logging.basicConfig(level=logging.INFO, format=fmt)

    test_count = 10000

    car_count_1 = 0
    car_count_2 = 0

    for _ in range(0, test_count):
        if get_car_1():
            car_count_1 += 1
        if get_car_2():
            car_count_2 += 1

    logging.info('Test count: {}'.format(test_count))
    logging.info('Cars by method 1: {}'.format(car_count_1))
    logging.info('Cars by method 2: {}'.format(car_count_2))


if __name__ == '__main__':
    main()
