#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 21:39:00 2020

@author: piumallick
"""
# Problem 412: Fizz Buzz
'''
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number 
and for the multiples of five output “Buzz”. For numbers which are multiples 
of both three and five output “FizzBuzz”.
'''

def fizzBuzz(n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i in range(1, n+1):
            if ((i % 3 == 0) and (i % 5 == 0)):
                result.append("FizzBuzz")
            elif (i % 3 == 0):
                result.append("Fizz")
            elif (i % 5 == 0):
                result.append("Buzz")
            else:
                result.append(str(i))
        return result
        
    
def fizzBuzz1(n): 
    resultArr = []
    for i in range(1, n+1):
        result = ""
        if (i % 3 == 0):
            result+="Fizz"
        if (i % 5 == 0):
            result+="Buzz"
        if (len(result) == 0):
            result+=str(i)
        resultArr.append(result)
    return resultArr
        
import dis

n = 15
#print(fizzBuzz1(n))
dis.dis(fizzBuzz)