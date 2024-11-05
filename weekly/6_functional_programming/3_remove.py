"""
Tuesday, November 5.th  2024

Task:
Write a function remove(x: Any, v: list) -> list that returns a list containing all the elements of v
that are different from x.
"""
from functools import reduce

def remove(x: any, v: list) -> list:
    """Returns v containing all elements that are different from x.
    >>> remove(3, ['a', 3, 4, 5, 6])
    ['a', 4, 5, 6]
    """
    return reduce(lambda a, b: a + [b],
                  filter(lambda y: y != x, v)
                  , [])

print(remove(3, ['a', 3, 4, 5, 6]))
