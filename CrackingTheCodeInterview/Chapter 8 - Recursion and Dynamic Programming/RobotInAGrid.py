# Robot in a grid:
# Imagine a robot sitting on the upper left corner of grid with r rows and c columns
# The robot can move only in 2 directions: right and down, but certain cells
# are off-limit, such that the robot cannot step on them. 
# Design an algorithm to find a path for the robot from the top left
# to the bottom right.

#Solution with Recursion O(2^r+c)

def getPath(maze):
    if maze == None or len(maze) == 0:
        return None
    path = [] 
    if isPath(maze, len(maze)-1, len(maze[0])-1, path):
        return path
    return None

def isPath(maze, row, col, path):
    #if out of bounds or not available, return
    if col < 0 or row < 0 or not maze[row][col]:
        return False
    
    isAtOrigin = (row == 0) and (col == 0)

    #if there's a path from the start to here, add my location
    if isAtOrigin or isPath(maze, row, col-1, path) or isPath(maze, row-1, col,path):
        point = (row,col)
        path.append(point)
        return True

    return False

# Testing    
print(getPath([[True, True],[True,True]]))
# Output: [(0, 0), (1, 0), (1, 1)]
