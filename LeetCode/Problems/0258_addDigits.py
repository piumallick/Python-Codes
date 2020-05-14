#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 11:01:50 2020

@author: piumallick
"""
# Problem 258: Add Digits
'''
Given a non-negative integer num, repeatedly add all its digits 
until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
'''

def addDigits(num):
    
    if (num < 9):
        return num
    
    if num % 9 == 0:
        return 9
    
    else:
        return (num % 9)


num = 100
print(addDigits(num))