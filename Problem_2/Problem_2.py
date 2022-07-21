"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""


def fib(n) -> list:
    a, b = 0, 1
    for __ in range(n):
        if a > n:
            break
        elif a % 2 == 0:
            yield a
        a, b = b, a + b


print(sum(list(fib(4000000))))
