"""
Module with range-based for-loop functions.

Author: Jianni Hu
Date: 2020.11.28
"""

def factorial(n):
    """
    Returns n! = n * (n-1) * (n-2) ... * 1
    
    0! is 1.  Factorial is undefined for integers < 0.
    
    Examples:
        factorial(0) returns 1
        factorial(2) returns 2
        factorial(3) returns 6
        factorial(5) returns 120
    
    Parameter n: The integer for the factorial
    Precondition: n is an int >= 0
    """
    mul=1
    
    for i in range(1,n+1):
        mul*=i
        
    return mul


def revrange(a,b):
    """
    Returns the tuple (b-1, b-2, ..., a)
    
    Note that this tuple is the reverse of tuple(range(a,b))
    
    Parameter a: the "start" of the range
    Precondition: a is an int <= b
    
    Parameter b: the "end" of the range
    Precondition: b is an int >= a
    """
    result=()
    tup=tuple(range(a,b))
    n=len(tup)
    
    for i in range(n):
        result+=(tup[n-i-1],)
    
    return result
