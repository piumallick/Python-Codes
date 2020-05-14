#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 10:53:33 2020

@author: piumallick
"""
# Problem 208: Implement Trie (Prefix Tree)
'''
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
'''

class TreeNode:
    
    def __init__(self, value):
        self.value = value
        self.children = {}
        self.end = False

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode(None)
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        parent = self.root
        for i, char in enumerate(word):
            if char not in parent.children:
                parent.children[char] = TreeNode(char)
            parent = parent.children[char]
            if i == len(word) - 1:
                parent.end = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        parent = self.root
        for char in word:
            if char not in parent.children:
                return False
            parent = parent.children[char]
        return parent.end
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        parent = self.root
        for char in prefix:
            if char not in parent.children:
                return False
            parent = parent.children[char]
        return True
        


# Your Trie object will be instantiated and called as such:
obj = Trie()
word = "apple"
prefix = "ap"
obj.insert(word)
param_2 = obj.search(word)
param_3 = obj.startsWith(prefix)
Trie()
