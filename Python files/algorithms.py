from constants import moveRow, moveCol


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

    Stack = []
    cell = stop

    while cell is not None:
        Stack.append(cell)
        cell = From[cell[0]][cell[1]]

    while len(Stack):
        row, col = Stack[-1]
        Stack.pop()
        grid[row][col].changeColor(colors.yellow)



def Dfs():
    pass



def Astar():
    pass