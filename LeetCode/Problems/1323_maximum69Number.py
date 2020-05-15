#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 00:31:44 2020

@author: piumallick
"""
# Problem 1323: Maximum 69 Number

'''
Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit
(6 becomes 9, and 9 becomes 6).

Example 1:

Input: num = 9669
Output: 9969
Explanation: 
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666. 
The maximum number is 9969.
Example 2:

Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.
Example 3:

Input: num = 9999
Output: 9999
Explanation: It is better not to apply any change.
'''
def maximum69Number (num):
    numStr = str(num)
    lst = [i for i in numStr]
    
    for i in range(len(numStr)):
        if (lst[i] == '6'):
            lst[i] = '9'
            break
        
    return int(''.join(lst))

# Testing
num = 9669 
print(maximum69Number(num))