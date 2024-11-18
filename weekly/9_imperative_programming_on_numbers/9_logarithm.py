"""
Monday, November 18.th  2024

Task:
Write a function logarithm(n: int, m: int) -> int that returns the integer base-m logarithm of n. If
unspecified, m should be 2.
"""

def logarithm(n: int, m: int) -> int:
    """
    Returns the integer base-m logarithm of n.
    >>> logarithm(2, 64)
    6
    """

    i = 0
    while m != 1:
        m = m//n
        i = i + 1
    return i

print(logarithm(2, 64))

