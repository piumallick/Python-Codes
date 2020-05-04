#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 22:49:19 2020

@author: piumallick
"""

# Day 2 Challenge
"""
Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

Example: 

Input: 19
Output: true
"""

     
'''
 
 let num = 123
 let sum = 0
 do while sum is not 1 {
     do while num is greater than one digit number {
         get number at index 1 of num
         num = num // 10
         calculate sum
     } 
     calculate sum for the last digit in num
 }
 
'''

def isHappyNumber(num):
    sum = 0
    numset = set()
    while (sum != 1 and (num not in numset)):
        numset.add(num)
        sum = 0
        while (num > 9):
            rem = num % 10
            rem_square = (rem ** 2)
            sum += rem_square
            num = num // 10
        sum += (num ** 2)
        num = sum
        #print(numset)
    return sum == 1


# Testing

if (isHappyNumber(2)):
     print('Happy Number')
else:
    print('Not a Happy Number')

    
            



