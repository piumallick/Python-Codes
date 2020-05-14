#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 23:05:14 2020

@author: piumallick
"""
# Problem 121: Best Time to Buy and Sell Stock
'''
Say you have an array for which the ith element 
is the price of a given stock on day i.

If you were only permitted to complete at most one 
transaction (i.e., buy one and sell one share of the stock),
design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''

def maxProfit(prices):
    
    if (len(prices) < 2):
        return 0
    
    lowestPrice = None
    bestProfit = 0
     
    for i in range(len(prices) - 1):
         currentDay = prices[i]
         nextDay = prices[i + 1]
         if (nextDay > currentDay):
             if (lowestPrice == None):
                 lowestPrice = currentDay
                 bestProfit = (nextDay - currentDay)
             else:
                 lowestPrice = min(lowestPrice, currentDay)
                 bestProfit = max(bestProfit, (nextDay - lowestPrice))
    return bestProfit
    
# Testing  
prices = [7,6,4,3,1]
print(maxProfit(prices))