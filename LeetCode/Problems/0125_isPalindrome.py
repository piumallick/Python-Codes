#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 23:52:50 2020

@author: piumallick
"""
# Problem 125: Valid Palindrome
'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
'''
def isPalindrome(s):
    
    s = (''.join(e for e in s if e.isalnum())).lower()
    if (s == s[::-1]):
        #print(s)
        #print(s[::-1])
        return True
    return False

# Testing
s = "A man, a plan, a canal: Panama"
s1 = "race a car"
print(isPalindrome(s1))
