#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 18:53:10 2020

@author: piumallick
"""

# Problem 1.2
# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

def isPermutation(s1, s2):
    
    # String length cannot be more than 256
    if len(s1) > 256: # Unicode charset range
        return False
    
    if (len(s1) != len(s2)):
        return False
    
    if (sorted(s1) == sorted(s2)):
        return True
    
    return False
    
# Driver Code
String1 = 'dog'
String2 = 'god'
print(isPermutation(String1, String2))

Str1 = 'abcd'
Str2 = 'efgh'
print(isPermutation(Str1, Str2))

s1 = 'abcd'
s2 = 'abbsc'
print(isPermutation(s1, s2))

s1 = 'a'
s2 = 'a'
print(isPermutation(s1, s2))

s1 = 'hydroxydeoxycorticosterones'
s2 = 'hydroxydesoxycorticosterone'
print(isPermutation(s1, s2))

s1 = 'basiparachromatin'
s2 = 'marsipobranchiata'
print(isPermutation(s1, s2))

# Output:
# True
# False
# False