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
    row = 0
    col = len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == element:
            return "Element is present in the index position: " , [row, col]
        elif matrix[row][col] > element:
            col -= 1
        else:
            row += 1
    return "Element not found"
    
    
# Testing - 1 
            
matrix = [[15, 20, 40, 85], [20, 35, 80, 95], [30, 55, 95, 105], [40, 80, 100, 120]]
element = 105
print(findElement(matrix, element))

# Output

# ('Element is present in the index position: ', [2, 3])

# Testing - 2

matrix = [[15, 20, 40, 85], [20, 35, 80, 95], [30, 55, 95, 105], [40, 80, 100, 120]]
element = 5
print(findElement(matrix, element))

# Output

# Element not found
