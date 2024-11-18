"""
Monday, November 18th. 2024

Task:
Write a function is_prime(n: int) -> bool that checks whether n is prime.
"""

def is_prime(n: int) -> bool:
    """
    Checks whether n is prime.
    >>> is_prime(17389)
    True
    >>> is_prime(17388)
    False
    """
    
    i = 2  
    while i <= n//2:
        if n % i == 0:
            return False
        i = i + 1
    return True

