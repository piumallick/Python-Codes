#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 10:16:28 2019

@author: piumallick
"""
"""
Python Program to find Simple Interest

Simple interest formula is given by:
Simple Interest = (P x T x R)/100
Where,
P is the principle amount
T is the time and
R is the rate

EXAMPLE1:
Input : P = 10000
        R = 5
        T = 5
Output :2500
We need to find simple interest on 
Rs. 10,000 at the rate of 5% for 5 
units of time.

EXAMPLE2:
Input : P = 3000
        R = 7
        T = 1
Output :210
"""
# Assigning the values

P = 10000
T = 5
R = 5

# Calculating the simple interest
SI = (P*T*R)/100;

print('The Simple Interest is:',SI)

# Sample Output
# The Simple Interest is: 2500.0