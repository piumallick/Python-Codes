#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 18:09:25 2020

@author: piumallick
"""
# Problem 1.1
# isUnique: Implement an algorithm to determine if a string has all unique characters. 
# WHat if you cannot use additional data structures?


def isUniqueChars(string):
    # String length cannot be more than 256
    if len(string) > 256: # Unicode charset range
        return False
    
    character_set = [False] * 128 # ASCII char range
    
    for i in range (0, len(string)):
        value = ord(string[i])
        if character_set[value]:
            return False
        character_set[value] = True
    return True

# Driver Code
string1 = 'abcd'
print('String1: "abcd" has unique characters - ', isUniqueChars(string1))

string2 = 'abbcgdhh'
print('String2: "abbcgdhh" has unique characters - ', isUniqueChars(string2))

# Output
# String1: "abcd" has unique characters -  True
# String2: "abbcgdhh" has unique characters -  False

# Complexity of this algorithm - O(n)