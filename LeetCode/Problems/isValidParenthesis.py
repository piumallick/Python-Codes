#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 16:50:28 2020

@author: piumallick
"""

# Problem 20: Valid Parenthesis

"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_parenthesis = {'(', '{', '['}
        closed_parenthesis = {')', '}', ']'}
        for parenthesis in s:
            if len(s) == 0 and parenthesis in closed_parenthesis:
                return False
            else:
                if parenthesis == ')' and stack[-1] == '(':
                    stack.pop()
                elif parenthesis == '}' and stack[-1] == '{':
                    stack.pop()
                elif parenthesis == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(parenthesis)
        return True if len(stack) == 0 else False

s = "(){}[]"
print(isValid(s))
# Output: True
