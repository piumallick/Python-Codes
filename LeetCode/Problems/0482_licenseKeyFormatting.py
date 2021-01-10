#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 19:48:24 2021

@author: piumallick
"""
# Leetcode Problem : 482 - License Key Formatting

'''
You are given a license key represented as a string S which 
consists only alphanumeric character and dashes. 
The string is separated into N+1 groups by N dashes.

Given a number K, we would want to reformat the strings 
such that each group contains exactly K characters, 
except for the first group which could be shorter than K, 
but still must contain at least one character. 
Furthermore, there must be a dash inserted between two 
groups and all lowercase letters should be converted to uppercase.

Given a non-empty string S and a number K, format the string 
according to the rules described above.
'''

def licenseKeyFormatting(S, K):
    counter = 0
    license_key = []
    for char in reversed(S):
        if char != '-':
            if counter == K:
                license_key.append('-')
                counter = 0
            license_key.append(char.upper())
            counter += 1
    return ''.join(reversed(license_key))
        
# Testing
    
S1 = "5F3Z-2e-9-w"
K1 = 4  
print(licenseKeyFormatting(S1, K1))
# Output: 5F3Z-2E9W

S2 = "2-5g-3-J"
K2 = 2
print(licenseKeyFormatting(S2, K2))
# Output: 2-5G-3J

