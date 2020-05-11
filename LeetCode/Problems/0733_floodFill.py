#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 10:52:56 2020

@author: piumallick
"""
# Problem 733: Flood Fill

'''
An image is represented by a 2-D array of integers, 
each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column)
 \of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, 
plus any pixels connected 4-directionally to the starting pixel o
f the same color as the starting pixel, plus any pixels connected 4-directionally 
to those pixels (also with the same color as the starting pixel), and so on. 
Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
'''

def floodFill(image, sr, sc, newColor):
    
    row_length = len(image)
    col_length = len(image[0])
    color = image[sr][sc]
    
    if (color == newColor):
        return image
    
    def floodFillConditions(row, col):
        if (image[row][col] == color):
            image[row][col] = newColor
            if (row >= 1):
                floodFillConditions(row - 1, col)
            if (row + 1 < row_length):
                floodFillConditions(row + 1, col)
            if (col >= 1):
                floodFillConditions(row, col - 1)
            if (col + 1 < col_length):
                floodFillConditions(row, col + 1)
            
    
    floodFillConditions(sr, sc)
    return image

# Testing
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2
print(floodFill(image, sr, sc, newColor))