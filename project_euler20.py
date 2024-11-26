#!/bin/python3


def main():
    product = 1
    for i in range(1, 101):
        product *= i

    product_str = str(product)
    sum = 0
    for c in product_str:
        sum += int(c)

    print(sum)

if __name__ == '__main__':
    main()
