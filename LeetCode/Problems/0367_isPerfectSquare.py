#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 08:51:33 2020

@author: piumallick
"""
# Problem 367: Valid Perfect Square
'''
Given a positive integer num, write a function which returns True 
if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
'''
def isPerfectSquare(num):
        if (num < 2):
            return True
        # Using Binary search (for optimization)
        left = 2
        right = num
        while (left <= right):
            mid = (left + right)//2
            if ((mid ** 2) == num):
                return True
            elif ((mid ** 2) < num):
                left = mid + 1
            else:
                right = mid - 1
        return False
    
def isPerfectSquare2(num):
    if (num < 2):
        return True
    i = 2
    # Not so efficient; Linear Search
    while (i <= num):
        if ((i ** 2) == num):
            return True
        i = i + 1
    return False
    
# Driver Code:
num1 = 16
num2 = 14
print(isPerfectSquare(num1))
print(isPerfectSquare(num2))
print(isPerfectSquare2(num1))
print(isPerfectSquare2(num2))
        
        