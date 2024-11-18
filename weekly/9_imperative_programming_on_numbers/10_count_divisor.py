"""
Monday, November 18.th  2024

Task:
Write a function count_divisors(n: int) -> int that returns the number of divisors of n.
"""


def count_divisors(n: int) -> int:
    """
    Returns the number of divisors of n. For n > 1.
    >>> count_divisors(6)
    4
    """
    i = 1
    divisors = 1 
    while i <= n//2:
        if n % i == 0:
            divisors = divisors + 1
        i = i + 1 
    return divisors 
