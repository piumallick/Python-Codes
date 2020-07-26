# Magic Index
# A magic index in an array A[1.... n-1] is defined to be an index such that A[i] = i. 
# Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.

# For distinct values in the array
# Brute Force method 
# Linear Scan - Time Complexity: O(n), Space Complexity: O(1)
def magicIndexBruteForce(n):
  for i in range(len(n)-1):
    if n[i] == i:
      return i
  return -1
#####################################################################

# For distinct values in the array
# Binary Search - Time Complexity: O(log n), Space Complexity: O(1)
def magicIndexBinarySearch(n):
  return magic(n, 0, len(n)-1)

def magic(n, start, end):
  #start, end = 0, len(n) - 1
  if end < start:
    return -1
  mid = (start + end) // 2
  if n[mid] == mid:
    return mid
  elif n[mid] < mid:
    return magic(n, mid + 1, end)
  else:
    return magic(n, start, mid - 1)
#####################################################################

# What if the values are not distinct? 
# That means, duplicates exist in the array.
# Modified Binary Search - Time Complexity: O(log n), Space Complexity: O(1)
def magicIndexBinarySearchModified(n):
  return magicFast(n, 0, len(n)-1)

def magicFast(n, start, end):
  if end < start:
    return -1
  midIndex = (start + end) // 2
  midVal = n[midIndex]
  if midVal == midIndex:
    return midIndex
  
  # Search Left
  leftIndex = min(midIndex - 1, midVal)
  left = magicFast(n, start, leftIndex)
  if left >= 0:
    return left
  # Search Right
  rightIndex = max(midVal, midIndex + 1)
  right = magicFast(n, rightIndex, end)
  return right
#####################################################################
# Testing
n = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]
n1 = [-40, -20, -1, 1, 2, 3, 7, 7, 7, 12, 13]
print(magicIndexBruteForce(n))
print(magicIndexBinarySearch(n))
print(magicIndexBinarySearchModified(n1))

  
