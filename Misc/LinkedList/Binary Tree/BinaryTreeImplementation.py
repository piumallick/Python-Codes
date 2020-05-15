#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 18:25:09 2020

@author: piumallick
"""

# Binary Tree Implementation

class Node(object):
    
    # Defining constructor
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinaryTree(object):
    
    def __init__(self, root):
        self.root = Node(root)
        
    """Helper function - Printing Tree"""
    def printTree(self, traversal_type):
        if traversal_type == "PreOrder":
            print("PreOrder Traversal:")
            return self.preorderTraversal(tree.root, "")
        else:
            print("Traversal type" + traversal_type + "is not supported in Binary Tree.")
            return False
            
   
    def preorderTraversal(self, start, traversal):
        """PreOrder Traversal""" 
        """Root -> Left -> Right"""
        if start:
            traversal += str(start.value) + " - "
            traversal = self.preorderTraversal(start.left, traversal)
            traversal = self.preorderTraversal(start.right, traversal)
        return traversal
        
    

# Testing
        
#               1
#             /   \
#            /     \
#           /       \
#          2         3
#        /   \      /  \
#       4     5    6    7
#                         \
#                          8        


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)
print(tree.printTree("PreOrder"))
        
        