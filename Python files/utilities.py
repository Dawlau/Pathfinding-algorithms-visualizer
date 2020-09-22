

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


# returns absolute path ot HowToUse.txt, relative to a Python file
def pathToHowToUse():
    import pathlib
    return pathlib.Path(__file__).parent.parent.joinpath("HowToUse.txt")


# converts matriceal coordinates to cartesian coordinates
def MatricealToCartesian(coords):
    from cell import side
    return (coords[0] * side, coords[1] * side)


# converts cartesian coordinates to matriceal coordinates
def CartesianToMatriceal(coords):
    from cell import side
    return (coords[0] // side, coords[1] // side)