#!/bin/python3


def main():
    prev_seq = {}
    longest_seq = 0
    starting_num = 0
    for n in range(1, 1000000):
        curr_seq = []
        curr_n = n
        curr_seq.append(curr_n)
        while curr_n != 1:
            try:
                curr_seq += prev_seq[curr_n][1:]
                break
            except KeyError:
                pass

            if curr_n % 2 == 0:
                curr_n = int(curr_n / 2)
            else:
                curr_n *= 3
                curr_n += 1
            curr_seq.append(curr_n)

        for idx in range(0, len(curr_seq)):
            try:
                prev_seq[curr_seq[idx]]
                break
            except:
                prev_seq[curr_seq[idx]] = curr_seq[idx:]

        print(n, curr_seq)

        if len(curr_seq) > longest_seq:
            longest_seq = len(curr_seq)
            starting_num = n

    print(longest_seq, starting_num)

if __name__ == '__main__':
    main()
