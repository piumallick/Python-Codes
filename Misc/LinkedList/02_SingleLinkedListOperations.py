#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 23:18:44 2020

@author: piumallick
"""

# Linked List - Implementation

class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None    # Initialization
        
class linked_list:
    nodeCount = 0
    def __init__(self):
        self.head = node()  # Defining constructor (Placeholder to allow the first pointer in the list)
        
    def append(self, data):
        new_node = node(data)
        curr = self.head
        while (curr.next != None):
            curr = curr.next
        curr.next = new_node
        self.nodeCount+=1
        #print('NodeCount:' , self.nodeCount)
    
# check this one    
    def length(self):     # Not passing any parameters, other than the instance of the class
        #print('NodeCount:' , self.nodeCount)
        return self.nodeCount
        
        
    def display(self):
        elements = []
        curr_node = self.head
        while (curr_node.next != None):
            curr_node = curr_node.next
            elements.append(curr_node.data)
        print(elements)
        
    
    def deleteDuplicates(self):
        curr = self.head
        prev = curr
        
        while (curr != None):
            if (curr.data == prev.data):
                prev.next = curr.next
                curr = curr.next
            else:
                curr = curr.next
                prev = prev.next
        return curr
    
    # This is not working    
    def get(self, index):
        if (index >= self.length()):
            print("ERROR: 'Get' Index Out Of Range!")
            return None
        curr_idx = 0
        curr_node = self.head
        while (True):
            curr_node = curr_node.next
            if (curr_idx == index):
                return curr_node.data
            curr_idx += 1
      
    def erase(self, index):
        if(index >= self.length()):
            print("ERROR: 'Erase' Index Out Of Range!")
            return
        curr_idx = 0
        curr_node = self.head
        while True:
            last_node = curr_node
            curr_node = curr_node.next
            if (curr_idx == index):
                last_node.next = curr_node.next
                return
            curr_idx += 1
            
        
# Testing
my_list = linked_list()

# my_list.display()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(4)
my_list.length()
my_list.display()
my_list.deleteDuplicates()
my_list.display()
#my_list.get(2)
my_list.erase(7)
my_list.display()
my_list.length()

