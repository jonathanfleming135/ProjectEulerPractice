#!/bin/python3
non_an_sums = []


def main():
    abudant_nums = []
    sqrt = 4
    max_non_an_sum = 28123
    for n in range(12, max_non_an_sum+1):
        if sqrt * sqrt < n:
            sqrt += 1
        if isAbudant(n, sqrt):
            abudant_nums.append(n)

    an_sums = {}
    for an1 in abudant_nums:
        for an2 in abudant_nums:
            an_sums[an1+an2] = True

    non_an_sum = 0
    my_non_an_sums = []
    for n in range(1, max_non_an_sum+1):
        try:
            if an_sums[n]:
                continue
        except KeyError:
            non_an_sum += n
            my_non_an_sums.append(n)

    print(non_an_sum)

def isAbudant(n: int, sqrt: int) -> bool:
    factors = set()
    factors.add(1)
    for possible_divisor in range(2, sqrt+1):
        if n % possible_divisor == 0:
            factor1 = possible_divisor
            factor2 = int(n / factor1)
            factors.add(factor1)
            factors.add(factor2)

    return sum(factors) > n


if __name__ == '__main__':
    main()
