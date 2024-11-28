#!/bin/python3


def main():
    prev_fib = 1
    curr_fib = 1
    next_fib = prev_fib + curr_fib
    idx = 3
    while len(str(next_fib)) < 1000:
        prev_fib = curr_fib
        curr_fib = next_fib
        next_fib = prev_fib + curr_fib
        idx += 1
        print(next_fib)

    print(idx)


if __name__ == '__main__':
    main()
