# https://en.wikipedia.org/wiki/Diversification_(finance)

import random
import logging

PROFIT_PROBABLITY = 0.5

PROFIT_PERCENT = 0.8
LOSS_PERCENT = 0.6


def trade_security(money, security_number):
    money_each = float(money) / security_number

    money = 0
    for i in range(0, security_number):
        money += trade_one_security(money_each)
    return money


def trade_one_security(money):
    if random.random() > PROFIT_PROBABLITY:
        money *= (1 - LOSS_PERCENT)
    else:
        money *= (1 + PROFIT_PERCENT)
    return money


def trade(money, security_number):
    for i in range(1, 53):
        money = trade_security(money, security_number)
        logging.info('after trade {} times, money: {}'.format(i, money))
    return money


def main():
    fmt = "%(asctime)s %(filename)s [%(lineno)d][%(levelname)s] %(message)s"
    logging.basicConfig(level=logging.INFO, format=fmt)

    money = 10000
    logging.info('initial money: {}'.format(money))

    money = trade(money, 10)
    money = format(money, ',')
    logging.info('final money: {}'.format(money))


if __name__ == '__main__':
    main()
