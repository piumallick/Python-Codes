#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 10:58:11 2020

@author: piumallick
"""
# Problem 231: Power of 2
'''
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false
'''

def isPowerOfTwo(n):
    if (n == 0):
        return False
    if (n ==  1):
        return True
    while ((n % 2) == 0):
        n /= 2
        #print('n:',n)
    if (n == 1):
        return True
    else:
        return False
    
def isPowerOfTwo2(n):
        """
        :type n: int
        :rtype: bool
        """
        if (n <= 0):
            return False
        while (n):
            if (n == 1):
                return True
            if ((n % 2) == 0):
                n /= 2
            else:
                return False
        return True
    

n = 64
print(isPowerOfTwo(n))
print(isPowerOfTwo2(n))