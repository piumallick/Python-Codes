#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 08:44:31 2020

@author: piumallick
"""

# Problem 383: Ransom note
'''
Given an arbitrary ransom note string and another string containing letters 
from all the magazines, write a function that will return true if the ransom 
note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
'''

import collections
def canConstruct(ransomNote, magazine):
    
    ransomNoteCount = collections.Counter(ransomNote)
    
    for key, value in ransomNoteCount.items():
        if (value > magazine.count(key)):
            return False
    return True


def canConstruct2(ransomNote, magazine):
    for i in set(ransomNote):
        if ransomNote.count(i) > magazine.count(i):
            return 0
    return 1


ransomNote = "aa ba"
magazine = "aab abb"
print(canConstruct(ransomNote,magazine))
