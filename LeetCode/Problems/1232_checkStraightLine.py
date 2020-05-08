#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 09:14:43 2020

@author: piumallick
"""
# Problem 1232: Check If It Is a Straight Line

'''
You are given an array coordinates, coordinates[i] = [x, y], 
where [x, y] represents the coordinate of a point. 
Check if these points make a straight line in the XY plane.

Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false

Constraints:

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point

'''

def checkStraightLine(coordinates):
        
        if (len(coordinates) == 2):
            return True
        
        x0,y0 = coordinates[0]
        x1,y1 = coordinates[1]
        
        for i in range(2, len(coordinates)):
            x,y = coordinates[i]
            
            if (y1-y0)*(x-x0) != (y-y0)*(x1-x0):
                return False
        return True
    
# Testing
coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
print(checkStraightLine(coordinates))
