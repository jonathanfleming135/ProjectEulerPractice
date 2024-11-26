#!/bin/python3


def main():
    for a in range(1, 1000):
        for b in range(1, 1000):
            for c in range(1, 1000):
                sum = a + b + c
                if isPythagoreanTriplet(a, b, c) and sum == 1000:
                    print(a * b * c)

def isPythagoreanTriplet(a: int, b: int, c: int) -> bool:
    return (a*a) + (b*b) == (c*c)

if __name__ == '__main__':
    main()
