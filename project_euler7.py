#!/bin/python3


def main():
    primes = [2, 3, 5, 7, 11, 13]
    while len(primes) < 10001:
        curr_prime = primes[-1]

        while True:
            curr_prime += 1
            if isPrime(primes, curr_prime):
                primes.append(curr_prime)
                break

    print(primes[10000])


def isPrime(primes: list[int], num: int) -> bool:
    for prime in primes:
        if num % prime == 0:
            return False
    return True


if __name__ == '__main__':
    main()
