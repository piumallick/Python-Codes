#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 09:18:29 2020

@author: piumallick
"""

# Problem 402: Remove K Digits
'''
Given a non-negative integer num represented as a string, 
remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form t
he new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. 
Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and 
it is left with nothing which is 0.
'''

def removeKdigits(num, k):
    '''
    result = ""
    
    # If there are no digits to remove
    if (k == 0):
        return result + num
    
    # If k is greater or equal to the length of the string 'num'
    if (len(num) <= k):
        return result 
    '''
    stack = []
    for cur in num:
        while k > 0 and len(stack) > 0 and stack[-1] > cur:
            stack.pop()
            k = k - 1
        stack.append(cur)
        print('while loop stack:',stack)
    if k > 0:
        stack = stack[:-k]
        #print('stack:',stack)
    return "".join(stack).lstrip("0") or "0"
    
    
 

# Testing
num = "54560006556"
k = 4
print(removeKdigits(num, k))
