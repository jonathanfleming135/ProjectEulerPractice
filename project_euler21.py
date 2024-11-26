#!/bin/python3


def main():
    sqrt = 1
    found_amicable_numbers = []
    for n in range(1, 10000):
        if sqrt * sqrt < n:
            sqrt += 1
        n_sum = getSumOfProperDivisors(n, sqrt)
        if getSumOfProperDivisors(n_sum, getSqrt(n_sum)) == n:
            if n not in found_amicable_numbers and n_sum not in found_amicable_numbers and n != n_sum:
                found_amicable_numbers.append(n)
                found_amicable_numbers.append(n_sum)

    print(sum(found_amicable_numbers))


def getSumOfProperDivisors(n: int, sqrt: int) -> int:
    # Every natural number is divisible by 1, so has at least 1 proper divisor
    proper_divisors = [1]
    for possible_divisor in range(2, sqrt):
        if n % possible_divisor == 0:
            divisor1 = int(n/possible_divisor)
            divisor2 = int(n/divisor1)
            proper_divisors.append(divisor1)
            proper_divisors.append(divisor2)

    return sum(proper_divisors)

def getSqrt(n: int) -> int:
    sqrt = 1
    while (sqrt * sqrt) < n:
        sqrt += 1
    return sqrt


if __name__ == '__main__':
    main()
