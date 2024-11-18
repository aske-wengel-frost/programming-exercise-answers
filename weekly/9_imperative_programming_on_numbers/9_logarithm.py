"""
Monday, November 18.th  2024

Task:
Write a function logarithm(n: int, m: int) -> int that returns the integer base-m logarithm of n. If
unspecified, m should be 2.
"""

def logarithm(n: int, m: int) -> int:
    """
    Returns the integer base-m logarithm of n.
    >>> logarithm(64, 2)
    6
    """

    i = 0
    while n != 1:
        n = n//m
        i = i + 1
    return i
