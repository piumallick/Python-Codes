#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 10:06:53 2019

@author: piumallick
"""

# Problem: Find the factorial of a given number
def factorial(n):
    
    # Finding factorial in a recursive manner
    if (n==1 or n==0):
        return 1
    else:
        return (n * factorial(n-1))
    
# Driver code
number = 4;
print("Factorial of",number , "is:",factorial(number))

    
# Sample output:
# Factorial of 4 is: 24