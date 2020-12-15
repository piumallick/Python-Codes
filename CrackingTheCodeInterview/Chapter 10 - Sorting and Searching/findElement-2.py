#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 18:15:24 2020

@author: piumallick
"""

# Sorted Matrix Search

"""
Given an M X N matrix in which each row and each column is sorted 
in ascending order. Write a method to find an element.
"""

# Naive Method (Brute Force)
def findElement(matrix, element):
    m = len(matrix)
        
    if m == 0:
        return False
    n = len(matrix[0])
    
    # Implentation of Binary Search
    low, high = 0, m * n - 1
    while low <= high:
        mid = (low + high) // 2
        mid_element = matrix[mid // n][mid % n]  
        if element == mid_element:
            return True
        elif element < mid_element:
            high = mid - 1
        else:
            low = mid + 1
    return False
        
    
    
    
# Testing - 1 
            
matrix = [[15, 20, 40, 85], [20, 35, 80, 95], [30, 55, 95, 105], [40, 80, 100, 120]]
element = 105
print(findElement(matrix, element))

# Output

# True

# Testing - 2

matrix = [[15, 20, 40, 85], [20, 35, 80, 95], [30, 55, 95, 105], [40, 80, 100, 120]]
element = 5
print(findElement(matrix, element))

# Output

# False
