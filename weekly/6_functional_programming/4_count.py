"""
Tuesday, November 5.th  2024

Task:
Write a function count(x:Any, v: list) -> int that counts the number of times that x appears in v.
"""

from functools import reduce

def count(x: any, v: list) -> int:
    """Counts the number of times that x appears in v.
    >>> count('a', ['a', 1 ,3 , 'b', 'a', 4 ,5 ,6])
    2
    """
    return reduce(lambda a, b: a + 1, 
                  filter(lambda y: y == x, v)
                  ,0)
    
print(count('a', ['a', 1 ,3 , 'b', 'a', 4 ,5 ,6]))
