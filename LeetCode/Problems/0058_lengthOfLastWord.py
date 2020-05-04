#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 23:06:23 2020

@author: piumallick
"""

"""
Problem 58
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""

def lengthOfLastWord(s):
    if (s == "" or s == " "):
        return 0
    s = " ".join(s.split())
    #print(s)
    sList = s.split()
    #print(sList)
    nWords = len(sList)
    
    if (nWords == 0):
        return 0
    lenthOfLastWord = len(sList[nWords-1])
    return lenthOfLastWord

# Testing
print(lengthOfLastWord(" Hello World"))
print(lengthOfLastWord("I am fine "))
print(lengthOfLastWord("Pennsylvania"))
print(lengthOfLastWord("          "))
