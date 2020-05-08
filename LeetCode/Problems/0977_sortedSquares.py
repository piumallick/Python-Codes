#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 15:01:17 2020

@author: piumallick
"""
# Problem 977: Squares of a Sorted Array
'''
Given an array of integers A sorted in non-decreasing order, 
return an array of the squares of each number, 
also in sorted non-decreasing order.

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 
Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.
'''

def sortedSquares(A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(0, len(A)):
            res.append(A[i] ** 2)
            i += 1
        return sorted(res)
    
def sortedSquares2(A):   
    return ([i*i for i in A])
 
# Testing
A = [1,2,3,4,5]
print(sortedSquares(A))

B = [-1, -2, 0, 7, 10]
print(sortedSquares2(B))