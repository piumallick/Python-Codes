#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 10:34:12 2019

@author: piumallick
"""

# Python Program to find out whether a given string is Plaindrome or not.
# Example:
# Input : malayalam
# Output : Yes

# Input : geeks
# Output : No

# The function returns the reverse of a string 
def reverse(string):
    return string[::-1]


def isPalindrome(string):
    # Calling the reverse function
    rev = reverse(string)
    
    if (string == rev):
        return True
    else:
        return False
    
# Driver Code
string = "radar"
output = isPalindrome(string)

if (output == 1):
    print(string,'is a Palindrome.')
else:
    print(string,'is not a Palindrome.')
    
string = "simple"
output = isPalindrome(string)

if (output == 1):
    print(string,'is a Palindrome.')
else:
    print(string,'is not a Palindrome.')
        
# Sample Output:
# radar is a Palindrome.
# simple is not a Palindrome.