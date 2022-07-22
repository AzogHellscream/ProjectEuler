"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def get_smallest_multiple(max_number: int) -> int:
    increment: int = 1
    while True:
        flag: bool = True
        for number in range(1, max_number):
            if increment % number != 0:
                increment += 1
                flag = False
                continue
        if flag:
            print('Found', increment)
            return increment


get_smallest_multiple(20)
