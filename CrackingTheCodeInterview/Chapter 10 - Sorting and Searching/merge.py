# Sorted Merge:
# Given 2 sorted arrays, A and B, A has a large enough buffer at the end to hold B. # Write a method to merge B into A in a sorted order.

def merge(A, B, countA, countB):
  # Last location of merged array
  indexMerged = countA + countB - 1
  # Last element in array A
  indexA = countA - 1
  # Last element in array B
  indexB = countB - 1

  # Merging of A and B, starting from the last element in each
  while indexB >= 0:
    if indexA >= 0 and A[indexA] > B[indexB]:
      A[indexMerged] = A[indexA]
      indexA -= 1
    else:
      A[indexMerged] = B[indexB]
      indexB -= 1
    indexMerged -= 1
  return A

# Testing
A = [2,3,4,6,0,0,0]
B = [1,5,7]
countA = 4
countB = 3
print(merge(A, B, countA, countB))

# Time Complexity: O(len(A) + len(B))
# Space Complexity : O(1)

