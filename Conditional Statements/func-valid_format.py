"""  
A function to check the validity of a numerical string

Author: Jianni Hu
Date: 2020.11.27
"""
import introcs


def valid_format(s):
    """
    Returns True if s is a valid numerical string; it returns False otherwise.
    
    A valid numerical string is one with only digits and commas, and commas only
    appear at every three digits.  In addition, a valid string only starts with
    a 0 if it has exactly one character.
    
    Pay close attention to the precondition, as it will help you (e.g. only numbers
    < 1,000,000 are possible with that string length).
    
    Examples: 
        valid_format('12') returns True
        valid_format('apple') returns False
        valid_format('1,000') returns True
        valid_format('1000') returns False
        valid_format('10,00') returns False
        valid_format('0') returns True
        valid_format('012') returns False
    
    Parameter s: the string to check
    Precondition: s is nonempty string with no more than 7 characters
    """
    result=False
    
    if introcs.isnumeric(s):
        if len(s)>=2 and s[0]=='0':
            pass
        elif ',' not in s and len(s)>=4:
            pass
        else:
            result=True
    elif len(s)>4 and s[-4]==',':
        if introcs.isnumeric(s[:-4]) and s[0]!='0':
            result=True
    
    return result
