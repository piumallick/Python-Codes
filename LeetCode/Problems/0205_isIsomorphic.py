#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 23:54:24 2020

@author: piumallick
"""

# Problem 205: Isomorphic Strings
'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
'''

'''
Algorithm:
    1. If the length of s and t are not same, then return False.
    2. If the length of s and t are same, traverse s and t simultaneously.
        2a. If the current character of s is seen for the  first time, then  the current character of 
            t should also have not been seen before.
            i. If the character in t has been visited, return False and flag this character as visited.
            ii. Store the mapping (in a dictionary, maybe)
        2b. Else part:
            If s(n) was seen before it was with t(n)
            If not return false and exit.
    3. return true
    

'''



def isIsomorphic(s, t):
    if (len(s) !=  len(t)):
        return False
    
    