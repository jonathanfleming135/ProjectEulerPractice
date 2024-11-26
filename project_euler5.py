#!/bin/python3


def main():
    smallest_num = 0

    while True:
        smallest_num += 20
        if isEvenlyDivisible(smallest_num, 20):
            break

    print(smallest_num)

def isEvenlyDivisible(numerator: int, max_divisor: int) -> bool:
    for num in range(2, max_divisor+1):
        if numerator % num != 0:
            return False
    return True

if __name__ == '__main__':
    main()
