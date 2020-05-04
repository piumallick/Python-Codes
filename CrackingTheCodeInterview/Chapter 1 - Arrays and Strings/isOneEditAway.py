#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 10:12:35 2020

@author: piumallick
"""

# Problem 1.5: One Way
"""
There are 3 types of edits that can be performed on strings:
    1. Insert a character
    2. Remove a character
    3. Replace a character
Given 2 strings, write a function to check if they are one edit (or zero edits) away.

Examples:
   pale, ple -> True
   pales, pale -> True
   pale, bale -> True
   pale, bae -> False
"""

def isOneEditAway(one, two):
    l1 = len(one) # Finding length of string 'one'
    l2 = len(two) # Finding length of string 'two'
    
    if (abs(l1 - l2) > 1): # If the absolute distance is more than 1
        return False       # then the strings cannot be one distance apart
    
    counter = 0 
    i = 0
    j = 0
    
    while (i < l1 and j < l2):
        if (one[i] != two[j]): # if the current characters do not match
            if (counter == 1):
                return False
            
            if (l1 > l2):
                i += 1
            elif (l1 < l2):
                j += 1
            else:
                i += 1
                j += 1
                
            counter += 1
            