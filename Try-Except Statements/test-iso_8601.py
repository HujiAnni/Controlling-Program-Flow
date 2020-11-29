"""  
A test script for the function iso_8601.

Author: Jianni Hu
Date: 2020.11.28
"""
import func
import introcs


def test_iso_8601():
    """
    Test procedure for the function iso_8601()
    """
    print('Testing iso_8601()')
    
    # Put your test cases here
    result = func.iso_8601('13:47:30')
    introcs.assert_equals(True,result)
    
    result = func.iso_8601('24:47:30')
    introcs.assert_equals(False,result)
    
    result = func.iso_8601(':47:30')
    introcs.assert_equals(False,result)
    
    result = func.iso_8601('23::30')
    introcs.assert_equals(False,result)

    result = func.iso_8601('23:47:')
    introcs.assert_equals(False,result)
    
    result = func.iso_8601('2:47:30')
    introcs.assert_equals(True,result)
    
    result = func.iso_8601('14:4:0')
    introcs.assert_equals(False,result)
    
    result = func.iso_8601('4:61:30')
    introcs.assert_equals(False,result)
    
    result = func.iso_8601('4:47:61')
    introcs.assert_equals(False,result)
    
    result = func.iso_8601('2425')
    introcs.assert_equals(False,result)
    
if __name__ == '__main__':
    test_iso_8601()
    print('Module func passed all tests.')