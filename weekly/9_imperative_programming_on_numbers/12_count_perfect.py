"""
Monday, November 18.th  2024

Task:
Write a function count_perfect(n: int) -> int that returns the number of perfect numbers smaller
than n.
"""

def count_perfect(n: int) -> int:
    """
    Returns the amount of perfect numbers smaller than n.
    >>> count_perfect(10)
    1
    >>> count_perfect(4)
    0
    """
    k = 1
    numbers_under_n = 0
    while k < n:
        i = 1
        total = 0
        while i <= k//2:
            if k % i == 0:
                total = total + i
            i = i + 1
        if k == total:
            numbers_under_n = numbers_under_n + 1
        k = k + 1

    return numbers_under_n
