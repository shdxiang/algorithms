#!/usr/bin/env python3

# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

import argparse


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n', '--number', help='limit number',
                        type=int, required=True)

    args = parser.parse_args()

    primes = [x for x in range(2, args.number+1)]

    index = 0
    while index < len(primes):
        p = primes[index]
        for i, n in enumerate(primes):
            if n != p and n % p == 0:
                del primes[i]
        index += 1

    print(primes)


if __name__ == '__main__':
    main()
