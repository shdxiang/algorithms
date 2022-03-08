#!/usr/bin/env python3

# https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80

import argparse


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-c', '--count', help='calculate count',
                        type=int, required=True)

    args = parser.parse_args()

    pi = 0

    for i in range(args.count):
        n = 2 * i + 1

        if i % 2 == 0:
            pi += 1 / n
        else:
            pi -= 1 / n

        if i % 10000000 == 0:
            print(pi * 4)

    print(pi * 4)


if __name__ == '__main__':
    main()
