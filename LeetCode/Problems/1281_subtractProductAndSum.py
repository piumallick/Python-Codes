#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 00:12:35 2020

@author: piumallick
"""
# Problem 1281: Subtract the Product and Sum of Digits of an Integer

'''
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 

Example 1:

Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
Example 2:

Input: n = 4421
Output: 21
Explanation: 
Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21

'''

def subtractProductAndSum(n):
    if (n == 0):
        return 0
    
    product = 1
    sum = 0
    while (n != 0):
        product = product * (n % 10)
        sum = sum + (n % 10)
        n = n // 10
    print('Sum: ', sum)
    print('Product: ',product)
    return (product - sum)

# Alternate way
def subtractProductAndSum1(n):
    product = 1
    for x in str(n):
        product = product * int(x)
    print(product)
    return (product - (sum(int(x) for x in str(n))))

# Testing
n = 114
print('Difference: ',subtractProductAndSum(n))
print('Difference: ',subtractProductAndSum1(n))