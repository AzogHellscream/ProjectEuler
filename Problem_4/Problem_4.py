"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def palindrome_check(number: int) -> bool:
    copy_number: int = number
    result: int = 0

    while number != 0:
        digit = number % 10
        result = result * 10 + digit
        number = int(number / 10)

    if result == copy_number:
        return True
    else:
        return False


def largest_palindrome_product() -> int:
    largest_palindrome_number: int = 0
    for first_number in range(999):
        for second_number in range(999):
            multiplication_result: int = first_number * second_number
            if palindrome_check(multiplication_result) and multiplication_result > largest_palindrome_number:
                largest_palindrome_number = multiplication_result
    return largest_palindrome_number


print(largest_palindrome_product())
