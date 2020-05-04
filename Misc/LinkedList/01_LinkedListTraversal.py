#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 15:42:47 2020

@author: piumallick
"""

# Linked List Traversal

# Node class
class Node:
    # Function to initialize the node object
    def __init__(self, data = None):
        self.data = data        # Assigning data
        self.next = None        # Initializing next as NULL
        
# LinkedList class        
class LinkedList:
    # Function to initialize LinkedList object (head)
    def __init__(self):
        self.head = None
    
    # This function prints the data of LinkedList, starting from the head    
    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    
llist = LinkedList()        # Start with an empty list
    
llist.head = Node('Monday')         # Node Monday created
second = Node('Tuesday')            # Node Tuesday created
third = Node('Wednesday')           # Node Wednesday created
fourth = Node('Thursday')           # Node Thursday created
    
llist.head.next = second;   # Linking first node with second
second.next = third;        # Linking second node with third
third.next = fourth;        # Linking third node with fourth
    
llist.printList()
    
    
    
    
    
        
        
            