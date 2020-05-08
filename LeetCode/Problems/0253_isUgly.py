#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 23:28:57 2020

@author: piumallick
"""
# Problem 263: Ugly Number
'''
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:

Input: 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: 8
Output: true
Explanation: 8 = 2 × 2 × 2
Example 3:

Input: 14
Output: false 
Explanation: 14 is not ugly since it includes another prime factor 7.
'''

def isUgly(num):
    if (num == 0):
        return False
    factor = [2,3,5]
    for x in factor:
        while ((num % x) == 0):
            num /= x
            print('num:',num)
    return num == 1   

# Testing    
num = 60
print(isUgly(num))
