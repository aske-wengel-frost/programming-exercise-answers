"""
Tuesday, November 5.th  2024

Task:
Write a function sum(v: list[int]) -> int that sums all the values in v.
"""

from functools import reduce

def sum(v: list[int]) -> int:
    """Sums all the values in v.
    >>> sum([1,3,4,6])
    14
    """
    return reduce(lambda x, y: x + y, v)

print(sum([1,3, 4, 6]))

