# https://en.wikipedia.org/wiki/Martingale_(betting_system)

import random
import time


def bet_to_win():
    count = 1
    while random.choice(['win', 'lose']) == 'lose':
        count += 1
    return count


def main():
    max_count = 0
    earning = 0
    while True:
        count = bet_to_win()
        if max_count < count:
            max_count = count
        earning = earning + 1
        print('earning: {}, count: {}, max count: {}, max stake: {}'.format(
            earning, count, max_count, pow(2, max_count - 1)))
        time.sleep(0.01)


if __name__ == '__main__':
    main()
