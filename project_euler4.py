#!/bin/python3

def main():
    pals = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            prod = i * j
            if isPalindrome(prod):
                pals.append(prod)

    pals.sort(reverse=True)
    print(pals[0], pals[1], pals[2])


def isPalindrome(num: int) -> bool:
    num_str = str(num)
    new_str = num_str[::-1]
    new_num = int(new_str)
    return new_num == num

if __name__ == '__main__':
    main()
