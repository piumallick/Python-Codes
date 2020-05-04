#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 15:26:27 2020

@author: piumallick
"""

# Problem 21
"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""
# Python offers the inbuilt function to perform this particular task 
# and performs the similar working in background as merge in naive method 
# and should be used when wanting to deal with this kind of problem.

from heapq import merge

def mergeTwoLists1(aList1, aList2):
    outputList = list(merge(aList1, aList2))
    return outputList

def mergeTwoLists2(aList1, aList2):
    outputList = sorted(aList1 + aList2)
    return outputList


aList1 = [1,2,4]
aList2 = [1,3,4]
print('1st List: ',aList1)
print('2nd List: ',aList2)
print('Merged Sorted List: (Way 1)',mergeTwoLists1(aList1,aList2))
print('Merged Sorted List: (Way 2)',mergeTwoLists2(aList1,aList2))