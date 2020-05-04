#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 10:51:51 2019

@author: piumallick
"""

"""
Python Program for cube sum of first n natural numbers
Print the sum of series 13 + 23 + 33 + 43 + …….+ n3 till n-th term.
"""

def sumOfSeries(n):
    sum = 0
    for i in range(1,n+1):
        sum += i*i*i
    
    return sum

# Driver Code
n = 10
print('The sum of the series is',sumOfSeries(n))

# Sample Output:
# The sum of the series is 3025