#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 08:50:52 2020

@author: piumallick
"""

# Problem 83: Remove Duplicates from Sorted List
'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
'''

class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        if (head == None):
            return head
        
        curr = head.next
        prev = head
        
        while (curr != None):
            if (curr.val == prev.val):
                prev.next = curr.next
                curr = curr.next
            else:
                curr = curr.next
                prev = prev.next
        return head
    

