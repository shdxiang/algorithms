#!/usr/bin/env python3

# https://en.wikipedia.org/wiki/Kelly_criterion


import random
import logging
import datetime

P = 0.501
Q = 1 - P
B = 1


def calc_f():
    return (B * P - Q) / B


def bet(money):
    if random.random() < P:
        return money * (1 + B)
    else:
        return -money


def main():
    fmt = "%(asctime)s %(filename)s [%(lineno)d][%(levelname)s] %(message)s"
    logging.basicConfig(level=logging.INFO, format=fmt)

    test_count = 1000

    inital_money = 1
    money_random = inital_money
    money_kelly = inital_money

    f_kelly = calc_f()

    for _ in range(0, test_count):
        if money_random > 0:
            f_random = random.random()
            money_random += bet(money_random * f_random)

        if money_kelly > 0:
            money_kelly += bet(money_kelly * f_kelly)

    logging.info('Test count: {}, initial money: {}'.format(
        test_count, inital_money))
    logging.info('Random F, final money: {}'.format(money_random))
    logging.info('Kelly F: {}, final money: {}'.format(f_kelly, money_kelly))


if __name__ == '__main__':
    main()
