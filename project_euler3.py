#!/bin/python3
import time

def main():
    previous_primes = [2]
    number = 600851475143
    factors = []
    while not foundAllFactors(factors, number):
        largest_factor = 1
        for factor in factors:
            largest_factor *= factor

        for i in range(2, number):
            if number % (i*largest_factor) == 0:
                factors.append(i)
                break

    factors.sort(reverse=True)
    for factor in factors:
        if isPrime(factor, previous_primes):
            print(factor)

def isPrime(num: int, prev_primes: list[int]) -> bool:
    for prime in prev_primes:
        if num % prime == 0:
            return False
    prev_primes.append(num)
    return True

def foundAllFactors(factors: list[int], num: int) -> bool:
    product = 1
    for factor in factors:
        product *= factor

    if product == num:
        return True

    return False


if __name__ == '__main__':
    main()
