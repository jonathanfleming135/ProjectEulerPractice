#!/bin/python3


def main():
    num = 1
    for i in range(1, 1001):
        num *= 2

    num_str = str(num)
    sum = 0
    for c in num_str:
        sum += int(c)

    print(sum)

if __name__ == '__main__':
    main()
