#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 11:26:37 2020

@author: piumallick
"""

# Problem 342: Power of 4
'''
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion? - using Bit operator?
'''


def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if (num <= 0):
            return False
        while (num):
            if (num == 1):
                return True
            if ((num % 4) == 0):
                num /= 4
            else:
                return False
        return True