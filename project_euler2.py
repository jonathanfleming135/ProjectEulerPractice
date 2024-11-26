#!/bin/python3

def main():
    sum = 0
    prev_prev_term = 1
    prev_term = 2
    sum += prev_term
    max_term = 4000000
    while prev_term + prev_prev_term < max_term:
        curr_term = prev_term + prev_prev_term
        if curr_term % 2 == 0:
            sum += curr_term
        prev_prev_term = prev_term
        prev_term = curr_term

    print(sum)


if __name__ == '__main__':
    main()
