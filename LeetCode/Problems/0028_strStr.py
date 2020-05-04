#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 21:10:17 2020

@author: piumallick
"""
# Problem 28: Implement strStr()
# Finding needle in the haystack

'''
Return the index of the first occurrence of needle in haystack, or -1 if needle 
is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
'''


def strStr1(haystack, needle):
    if (needle == ""):
        return 0
    index = haystack.find(needle)
    return index

def strStr(haystack, needle):
    return haystack.find(needle)
    
# Testing
haystack = ""
needle = ""
print(strStr1(haystack, needle))
print(strStr(haystack, needle))