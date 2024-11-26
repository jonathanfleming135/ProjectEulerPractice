#!/bin/python3


def main():
    nums_to_strings = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "fourty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
        100: "hundred",
        1000: "thousand"
    }

    sum = 0
    for num in range(1, 1001):
        num_str = str(num)
        num_word_str = ''
        if num <= 20:
            num_word_str += nums_to_strings[num]
        elif num < 100:
            if num_str[-1] == '0':
                num_word_str = nums_to_strings[num]
            else:
                ones_digit = int(num_str[-1])
                tens_digit = num - ones_digit
                num_word_str += nums_to_strings[tens_digit]
                num_word_str += nums_to_strings[ones_digit]
        elif num < 1000:
            ones_digit = int(num_str[2])
            tens_digit = int(num_str[1])
            hund_digit = int(num_str[0])
            num_word_str += nums_to_strings[hund_digit]
            num_word_str += nums_to_strings[100]
            if ones_digit != 0 or tens_digit != 0:
                num_word_str += "and"
                if tens_digit == 1:
                    num_word_str += nums_to_strings[(tens_digit * 10) + ones_digit]
                elif tens_digit != 0:
                    num_word_str += nums_to_strings[tens_digit * 10]

                if ones_digit != 0 and tens_digit != 1:
                    num_word_str += nums_to_strings[ones_digit]
        elif num == 1000:
            num_word_str += nums_to_strings[1]
            num_word_str += nums_to_strings[1000]
        print(num_word_str)
        sum += len(num_word_str)
        print(sum)
    print(sum)

if __name__ == '__main__':
    main()
