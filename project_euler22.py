#!/bin/python3


def main():
    with open('0022_names.txt', 'r') as f:
        all_names = f.read().replace('"', '').split(',')

    sorted_names = []
    for first_name in all_names:
        idx = 0
        for sorted_name in sorted_names:
            if first_name <= sorted_name:
                break
            idx += 1
        sorted_names.insert(idx, first_name)

    print(sorted_names)
    total_sum = 0
    for pos in range(1, len(sorted_names)+1):
        name = sorted_names[pos-1]
        curr_score = getNameVal(name) * pos
        total_sum += curr_score
        # print(curr_score)

    print(total_sum)
    print(getNameVal('COLIN'))


def getNameVal(name: str) -> int:
    name_sum = 0
    for c in name:
        name_sum += ord(c) % 64
    return name_sum

if __name__ == '__main__':
    main()
