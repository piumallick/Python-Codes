#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 20:07:46 2020

@author: piumallick
"""

# Problem 1.3
# Write a program to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold additional characters,
# and that you are given the "true" length of the string.

def replaceSpaces(string):
    
    string = string.split()
    s = '%20'
   
    s = s.join(string)
    return s
  
   
# Driver code
s1 =  'Mr. Johns Smith    '
print(replaceSpaces(s1))

s2 = "Piu  Mallick  "
print(replaceSpaces(s2))

# Output
# Mr.%20Johns%20Smith
# Piu%20Mallick

