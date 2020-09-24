

# takes a rectangle and (x, y) coordinates and returns if the point is inside the rectangle
def inRect(rect, coords):
    return rect.left <= coords[0] <= rect.right and rect.top <= coords[1] <= rect.bottom



# returns the contents of a specified file
def parseFile(file):

    with open(file, "r") as fin:
        
        line = fin.readline()
        text = line

        while line != "":
            line = fin.readline()
            text += line

    return text



# returns absolute path of root Directory, relative to a Python file
def rootDir():
    import pathlib
    return pathlib.Path(__file__).parent.parent



def fromRootFile(file):
    import pathlib
    return rootDir().joinpath(file)



# converts matriceal coordinates to cartesian coordinates
def MatricealToCartesian(coords):
    from cell import side
    return (coords[1] * side, coords[0] * side)


# converts cartesian coordinates to matriceal coordinates
def CartesianToMatriceal(coords):
    from cell import side
    return (coords[1] // side, coords[0] // side)



# check if specified row and col are in grid
def inGrid(grid, row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])



# returns the manhattan distance between A and B
def ManhattanDistance(A, B):
    return abs(A[1] - B[1]) + abs(A[0] - B[0])