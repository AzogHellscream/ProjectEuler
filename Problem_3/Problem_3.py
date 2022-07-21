"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
from math import sqrt


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i = i + 2

    return True


def get_largest_prime_factor(number: int) -> int:
    largest_prime_factor: int = 0
    for i in range(2, round(sqrt(number))):
        if number % i == 0 and is_prime(i):
            largest_prime_factor = i

    return largest_prime_factor


print('Largest prime factor of the number 600851475143 is', get_largest_prime_factor(600851475143))
