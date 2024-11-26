#!/bin/python3

def main():
    prev_primes = [2]
    max_prime = 2000000
    sqrt = 2
    for num in range(3, max_prime, 2):
        while sqrt * sqrt < num:
            sqrt += 1

        if isPrime(prev_primes, num, sqrt):
            prev_primes.append(num)

    sum = 0
    for prime in prev_primes:
        sum += prime

    print(sum)


def isPrime(prev_primes: list[int], num: int, sqrt: int) -> bool:
    for prime in prev_primes:
        if num % prime == 0:
            return False
        if prime >= sqrt:
            return True
    return True


if __name__ == '__main__':
    main()
