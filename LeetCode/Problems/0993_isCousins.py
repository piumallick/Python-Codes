#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 09:28:02 2020

@author: piumallick
"""

# Problem 993: Cousins in a Binary Tree
'''
In a binary tree, the root node is at depth 0, 
and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, 
but have different parents.

We are given the root of a binary tree with unique values, 
and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

Example 1:
Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Example 2:
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Example 3:
Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        xinfo = []
        yinfo = []
        #depth = 0
        #parent = None
        # Base case
        if root is None:
            return False
        
        self.dfs(root, x, y, 0, None, xinfo, yinfo)
        return xinfo[0][0] == yinfo[0][0] and xinfo[0][1] != yinfo[0][1]
    
    def dfs(self, root, x, y, depth, parent, xinfo, yinfo):
        if root is None:
            return False
        if (root.val == x):
            xinfo.append((depth, parent))
        if (root.val == y):
            yinfo.append((depth, parent))
            
        self.dfs(root.left, x, y, depth + 1, root, xinfo, yinfo)
        self.dfs(root.right, x, y, depth + 1, root, xinfo, yinfo)
        



        