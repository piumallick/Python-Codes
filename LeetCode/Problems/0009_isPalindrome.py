#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 15:46:03 2020

@author: piumallick
"""

# Problem 9: Palindrome Number
"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
"""

def isPalindrome(n):
    r = 0
    x = n
    if (n < 0):
        return False
    while (n > 0):
        a = n % 10
        r = (r * 10) + a
        n = n // 10
    print('x=',x)
    print('r=',r)
    if (x == r):
        return True
    else:
        return False
   
n = 121
print(isPalindrome(n))
    
        
        
