import random
import time


def main():
    n = 0
    while True:
        if random.choice([0, 1]) == 0:
            n = n + 1
        else:
            n = n - 1
        print(n)
        time.sleep(0.01)


if __name__ == '__main__':
    main()
