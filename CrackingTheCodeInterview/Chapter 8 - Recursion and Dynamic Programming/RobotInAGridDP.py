# Robot in a grid:

# Imagine a robot sitting on the upper left corner of grid with r rows and c columns
# The robot can move only in 2 directions: right and down, but certain cells
# are off-limit, such that the robot cannot step on them. 
# Design an algorithm to find a path for the robot from the top left
# to the bottom right.

# Solution with Memoization (Dynamic Programming): O(rc)

def getPathMemoized(maze):
  if maze == None or len(maze) == 0:
    return None
  path = []
  failedPoints = []

  if isPathMemoized(maze, len(maze)-1, len(maze[0])-1, path, failedPoints):
    return path
  return None

def isPathMemoized(maze, row, col, path, failedPoints):
  if col < 0 or row < 0 or not maze[row][col]:
    return False

  point = (row, col)

  isAtOrigin = (row == 0) and (col == 0)

  if isAtOrigin or isPathMemoized(maze, row, col-1, path, failedPoints) or isPathMemoized(maze, row-1, col, path, failedPoints):
    path.append(point)
    return True

  failedPoints.append(point)
  return False

# Testing
print(getPathMemoized([[True,True], [False,True]]))
# Output: [(0, 0), (0, 1), (1, 1)]



