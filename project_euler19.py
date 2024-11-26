#!/bin/python3


def main():
    num_sundays = 0
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
    months = {'jan': 31, 'feb': None, 'mar': 31,
              'apr': 30, 'may': 31, 'jun': 30,
              'jul': 31, 'aug': 31, 'sep': 30,
              'oct': 31, 'nov': 30, 'dec': 31}
    day_idx = 2
    for year in range(1901, 2001):
        for month in months.keys():
            if year % 4 == 0 and month == 'feb':
                months['feb'] = 29
            else:
                months['feb'] = 28
            for day_in_month in range(1, months[month]+1):
                today = days[day_idx]
                if day_in_month == 1 and today == 'sun':
                    num_sundays += 1
                day_idx = (day_idx + 1) % 7

    print(num_sundays)

if __name__ == '__main__':
    main()
