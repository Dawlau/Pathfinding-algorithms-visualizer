from constants import moveRow, moveCol

def buildPath(From, grid, start, stop):

    import colors

    Stack = []
    cell = From[stop[0]][stop[1]]
    prev = stop

    while cell != start:

        direction = None
        for dir in range(len(moveRow)):
            if (cell[0] + moveRow[dir], cell[1] + moveCol[dir]) == prev:
                if dir == 0:
                    direction = "up"
                elif dir == 1:
                    direction = "right"
                elif dir == 2:
                    direction = "down"
                else:
                    direction = "left"

        Stack.append((cell, direction))

        prev = cell
        cell = From[cell[0]][cell[1]]

    while len(Stack):
        cell, direction = Stack[-1]
        row, col = cell
        Stack.pop()
        grid[row][col].changeColor(colors.white)
        grid[row][col].addArrow(direction)



def Dijkstra():
    print("Dijkstra")



def Bfs(grid, start, stop, showSteps):

    from collections import deque
    import colors, utilities

    rows = len(grid)
    cols = len(grid[0])

    Deque = deque()

    seen = [] * rows
    From = [] * rows

    for row in range(rows):
        seen.append([False] * cols)
        From.append([None] * cols)

    Deque.append(start)
    seen[start[0]][start[1]] = True

    while len(Deque):

        row, col = Deque.popleft()

        for dir in range(len(moveRow)):
            newRow = row + moveRow[dir]
            newCol = col + moveCol[dir]

            if utilities.inGrid(grid, newRow, newCol) and not seen[newRow][newCol] and grid[newRow][newCol].color is not colors.black:
                seen[newRow][newCol] = True
                From[newRow][newCol] = (row, col)
                Deque.append((newRow, newCol))

    if not seen[stop[0]][stop[1]]:
        return 0

    buildPath(From, grid, start, stop)

    return 1


def Dfs():
    pass



def Astar():
    pass


def GreedyBestfs():
    pass