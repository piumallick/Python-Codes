#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 09:26:21 2020

@author: piumallick
"""
# Problem 278
# LeetCode 30 Day Challenge: May 1, 2020
# First Bad Version

'''
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version.
'''

def isBadVersion(version):
    print("version: ", version)
    if (version >= 98765321):
        return True
    else:
        return False
    
def firstBadVersion(n):
    start = 1
    end = n
    
    if (n == 0):
        return 0
    
    while ((start + 1) < end):
        mid = start + (end - start) // 2
        
        if (isBadVersion(mid) == True):
            end = mid     
        else:
            start = mid
            
 
    if isBadVersion(start):
        return start
    else:
        return end


def firstBadVersion3(n):
    left=1
    right=n
    while left<right:
        mid=left+(right-left)//2
        if isBadVersion(mid):
            right=mid
        else:
            left=mid+1
    return left
    
        
        
# Testing
import time

n = 9889988989
start_time = time.time()
print("firstBadVersion:", firstBadVersion(n))
print("--- %s seconds ---" % (time.time() - start_time))

#start_time = time.time()
#print("firstBadVersion:", firstBadVersion2(n))
#print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print("firstBadVersion:", firstBadVersion3(n))
print("--- %s seconds ---" % (time.time() - start_time))


'''
Algorithm:

    1. Assign start = 1, end = n
    2. if n = 0, return 0
    3. While (start + 1) < end:
        a. find the mid position
        b. if the mid position is equal to bad version, return the mid position (and assign end to mid)
        c. else assign mid position to start
        

'''
        
        
        
        
        
        
        