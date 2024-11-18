"""
Monday, November 18.th  2024

Task:
Write a function is_perfect(n: int) -> bool that checks whether n is a perfect number.
"""

def is_perfect(n: int) -> bool:
    """
    Checks whether n is a perfect number.
    >>> is_perfect(6)
    True
    """

    i = 1 
    total = 0
    while i <= n//2:
        if  n % i == 0:
            total = total + i
        i = i + 1
    return total == n
