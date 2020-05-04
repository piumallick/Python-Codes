#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 19:44:46 2020

@author: piumallick
"""

# Problem 344: Reverse String
'''
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array 
in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
'''


def reverseString(s):
    s.reverse()
    return s
 
# Testing
s = ["h","e","l","l","o"]
s1 = ["H","a","n","n","a","h"]
print(reverseString(s))
print(reverseString(s1))
 