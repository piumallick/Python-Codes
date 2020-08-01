# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and entire column are set to 0.

def setZeroes(matrix):

  if not matrix:
    return "No values in the matrix"

  row = [False] * len(matrix)
  column = [False] * len(matrix[0])
  
  # Store the row and column index with value 0
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      if matrix[i][j] == 0:
        row[i] = True
        column[j] = True
  
  # Nullify rows
  for i in range(0, len(row)):
    if row[i]:
      nullifyRow(matrix, i)
  # Nullify columns
  for j in range(0, len(matrix[0])):
    if column[j]:
      nullifyColumn(matrix, j)

  return matrix

def nullifyRow(matrix, row):
  for j in range(len(matrix[0])):
    matrix[row][j] = 0

def nullifyColumn(matrix, column):
  for i in range(len(matrix)):
    print(i, column)
    matrix[i][column] = 0

# Testing
matrix = [[1,2,3], [0,4,6], [9,7,5]]
matrix1 = []
print(setZeroes(matrix))
print(setZeroes(matrix1))
# Output: 
# [[0, 2, 3], [0, 0, 0], [0, 7, 5]] 
# No values in the matrix   

# Time Complexity: O(MN)
# Space Complexity: O(N)
