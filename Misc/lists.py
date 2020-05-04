# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 19:18:52 2018

@author: piuma
"""

#Take a list, say for example this one:
#
#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.
#
#Extras:
#
#Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it 
#and print out this new list.
#Write this in one line of Python.
#Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number
#given by the user.


def elements(aList):
    num = int(input("Choose a number: "))
    bList = []
    for i in aList:
        if i < num:     # or i < 5, as asked in the earlier part of the program
            bList.append(i)
    print (bList)


# Output check
#    
#a = elements([1,2,5,7,9,3,5])
#
#Choose a number: 7
#[1, 2, 5, 3, 5]
#
#a = elements([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
#
#Choose a number: 7
#[1, 1, 2, 3, 5]