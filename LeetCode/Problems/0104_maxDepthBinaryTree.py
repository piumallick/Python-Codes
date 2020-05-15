#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 20:12:03 2020

@author: piumallick
"""
# Problem 104: Maximum Depth of a Binary Tree

'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the 
longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
'''

class Node: 
    def __init__(self , val): 
          self.value = val  
          self.left = None
          self.right = None
    '''      
    def maxDepth(root):
        if root == None:
            return 0
    
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    '''
    def maxDepth2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        
        leftDepth = self.maxDepth2(root.left)
        rightDepth = self.maxDepth2(root.right)
        
        if leftDepth > rightDepth:
            return leftDepth + 1
        else:
            return rightDepth + 1

# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.right.left = Node(8)
root.right.left.right = Node(7)
print(root.maxDepth2(8))