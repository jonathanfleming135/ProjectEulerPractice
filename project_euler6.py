#!/bin/python3


def main():
    sum_of_squares = 0
    for i in range(1, 100+1):
        sum_of_squares += i*i

    sqaure_of_sum = 0
    for i in range(1, 100+1):
        sqaure_of_sum += i
    sqaure_of_sum = sqaure_of_sum * sqaure_of_sum

    print(sum_of_squares - sqaure_of_sum)

if __name__ == '__main__':
    main()
