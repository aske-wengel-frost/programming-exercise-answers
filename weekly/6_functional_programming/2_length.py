"""
Tuesday, November 5.th  2024

Task:
Write a function length(v: list) -> int that returns the length of v.
"""
from functools import reduce

def length(v: list) -> int:
    """Returns the length of v.
    >>> length(['a', 2, 3, 4]) 
    4
    """
    return reduce(lambda x, y: x + 1, v, 0)

print(length(['a', 2, 3, 4]))

