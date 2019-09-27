#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 10:59:35 2019

@author: piumallick
"""
# Python Program to find out the largest number in the array

# Function to find out the maximum number in the array

def largestNumber(arr, n):
    # Initialize the maximum element
    max = arr[0]
    
    #Traverse the array to find out the max element
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
            
    return max

# Driver Code
arr = [10, 20, 30, 50, 40, 90, 5]
n = len(arr)
print('The largest number in the array is',largestNumber(arr,n),'.')
    
    
