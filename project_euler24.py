#!/bin/python3


def main():
    digits = '0123456789'
    curr_size = 2
    permutations = set()
    permutations.add('01')
    permutations.add('10')
    while curr_size < len(digits):
        digit = digits[curr_size]
        new_permutations = []
        for permutation in permutations:
            for i in range(len(permutation)+1):
                new_permutation = permutation[:i] + digit + permutation[i:]
                new_permutations.append(new_permutation)

        permutations = new_permutations
        curr_size += 1

    permutations.sort()
    print(permutations[999999])


if __name__ == '__main__':
    main()
