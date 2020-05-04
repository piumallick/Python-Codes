#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 09:05:51 2020

@author: piumallick
"""
# Problem 771: Jewels and Stones
'''
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.
'''


def numJewelsInStones(J, S):
    Jset = set(J)
    #return sum(1 for stone in S if stone in Jset)
    return sum(s in Jset for s in S)



def numJewelsInStones2(J, S):
    Jset = set(J)
    return sum(1 for stone in S if stone in Jset)
    #return sum(s in Jset for s in S)


# Testing
import dis    

J = "aA"
S = "aAAbbbb"
#print(numJewelsInStones(J, S))

print("------------- numJewelsInStones ------------")
dis.dis(numJewelsInStones)

print("------------- numJewelsInStones ------------")
dis.dis(numJewelsInStones2)