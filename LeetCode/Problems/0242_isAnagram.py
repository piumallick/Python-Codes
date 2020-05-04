#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 13:28:35 2020

@author: piumallick
"""
# Problem 242: Valid Anagram

'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
'''
def isAnagram(s, t):
    
    if (sorted(s) == sorted(t)):
        return True
    else:
        return False
    
s = "anagram"
t = "nagaram"
print(isAnagram(s,t))