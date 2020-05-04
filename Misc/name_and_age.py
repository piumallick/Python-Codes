# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 19:22:40 2018

@author: piuma
"""

#Create a program that asks the user to enter their name and their age. 
#Print out a message addressed to them that tells them the year that they will turn 100 years old.
#
#Extras:
#
#Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
#(Hint: order of operations exists in Python)
#Print out that many copies of the previous message on separate lines. 
#(Hint: the string "\n is the same as pressing the ENTER button)

import datetime
now = datetime.datetime.now()
special_characters = "!,@,$,%,^,&,*,(,),_,-,+,=,~,`,{,},[,],\,|,:,;,<,>,.,/,?".split(",")

while True:
    name = input("Welcome! Please enter your name : ")
    try:
        name = int(name)
        print("It seems you have made a silly mistake. Please try again!!!")
    except ValueError:
        try:
            for i in special_characters:
                if i in name:
                    raise "Error in name."
            break        
            print("Go ahead!!")
        except:
            print("Special Character error.")
            pass
        
while True:
    try:
        age = int(input("Please enter your age : "))
        break
    except ValueError:
        print("Oops! This is not a valid integer..... Please try again.")
        
print("Hello! ", name)
print("Your age is ", age, "years.")
print("\nCurrent year is: %d" % now.year)
year = (now.year - age) + 100
string = "You will turn 100 years old in " + str(year) + ".\n"

extra = int(input("Please rate your enthusiasm level : Range(1 - 10) : "))
print( string * extra)
