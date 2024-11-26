#!/bin/python3


def main():
    triange_nums = [1, 3, 6]
    sqrt = 3
    while len(getAllFactors(triange_nums[-1], sqrt)) < 500:
        next_triange_num = triange_nums[-1] + len(triange_nums) + 1
        triange_nums.append(next_triange_num)
        while (sqrt*sqrt) < triange_nums[-1]:
            sqrt += 1

    print(triange_nums[-1])



def getAllFactors(num: int, sqrt: int) -> list[int]:
    factors = []
    for i in range(1, sqrt+1):
        if num % i == 0:
            factor1 = i
            factor2 = int(num / i)
            factors.append(factor1)
            factors.append(factor2)
    return factors



if __name__ == '__main__':
    main()
