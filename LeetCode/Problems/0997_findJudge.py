#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 08:44:46 2020

@author: piumallick
"""
# Problem 997: Find the Town Judge

'''
In a town, there are N people labelled from 1 to N. 
There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing 
that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label 
of the town judge.  Otherwise, return -1.

Example 1:

Input: N = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: N = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
Example 4:

Input: N = 3, trust = [[1,2],[2,3]]
Output: -1
Example 5:

Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
 

Note:

1 <= N <= 1000
trust.length <= 10000
trust[i] are all different
trust[i][0] != trust[i][1]
1 <= trust[i][0], trust[i][1] <= N
'''

def findJudge(N, trust):
    
    if (len(trust) < (N-1)):
        return -1
    valTrust = [0] * (N + 1)
    #print(valTrust)
    
    for input,output in trust:
        valTrust[input] = valTrust[input] - 1
        valTrust[output] = valTrust[output] + 1
    
    print(valTrust)
    #print(max(valTrust))
     
    for i, scores in enumerate(valTrust[1:], 1):
        if (scores == (N - 1)):
            return i
    return -1

#################################################
    
# Not working
    '''
import numpy as np

def findJudge2(N, trust):
    
    trustArray = np.array(trust)
    uniqueTrustArray = set(np.unique(trustArray))
    #print(uniqueTrustArray)
    
    
    trustingSet = set([col[0] for col in trust])
    #uniqueTrustingSet = set(np.unique(trustingSet))
    #print(trustingSet)
    
    setDiff = uniqueTrustArray.difference(trustingSet)
    #print(setDiff)
    
    #print(list(setDiff)[0])
    
    #for e in setDiff:
        #print(e)
   

    if (len(setDiff) == 1):
        return (list(setDiff)[0])
    else:
        return -1
'''
           
# Testing
#trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
#N = 4
#print(findJudge2(N, trust))

trust1 = [[1,2],[2,3]]
N1 = 3
print(findJudge(N1, trust1))