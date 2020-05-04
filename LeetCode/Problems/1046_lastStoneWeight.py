#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 22:49:32 2020

@author: piumallick
"""

# Problem 1046: Last Stone Weight
'''
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

 

Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
'''

def lastStoneWeight(stones):
    
    if (len(stones) == 1):
        return 1
    
    
    while (len(stones) > 1):
        sorted_stones = sorted(stones)
        print('sorted stones original:', sorted_stones)
        difference = (sorted_stones[-1] - sorted_stones[-2])
        print('difference:', difference)
        sorted_stones = sorted_stones[:len(sorted_stones)-2]
    
        if (difference != 0):
            sorted_stones.append(difference)
        
        print('sorted stones post-modification:',sorted_stones)
        
        stones = sorted_stones
    
    if (len(stones) == 0):
        return 0
    else:
        return stones[0]
    
    
# Testing
stones = [2,2]
print(lastStoneWeight(stones))