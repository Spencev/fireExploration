import random

def generateGrid(width, height, treeDensity, fireSources):
    grid = []
    for row in range(0, height):
        rowHold = []
        for column in range(0, width):
            if random.random() < treeDensity:
                rowHold.append("T")
            else:
                rowHold.append("O")
        grid.append(rowHold)
    fireList = []
    for fire in range(0, fireSources):
        yCoord = random.randint(1, height-1)
        xCoord = random.randint(1, width-1)
        if grid[yCoord][xCoord] == "O":
            grid[yCoord][xCoord] = "F"
        else:
            grid[yCoord][xCoord] = "B"
    grid[0][0] = "R"
    return grid

def updateGrid(grid):
    toChange = []
    rows = len(grid)
    columns = len(grid[0])
    for row in range(0, rows):
        for column in range(0, columns):
            if grid[row][column] == "B" and random.random() < 0.25:
                grid[row][column] = "F"
                direction = random.random()
                if direction < 0.25:
                    toChange.append([row + 1, column])
                    toChange.append([row + 2, column])
                elif direction < 0.50:
                    toChange.append([row - 1, column])
                    toChange.append([row - 2, column])
                elif direction < 0.75:
                    toChange.append([row, column + 1])
                    toChange.append([row, column + 2])
                else:
                    toChange.append([row, column - 1])
                    toChange.append([row, column - 2])
            if grid[row][column] == "F" or grid[row][column] == "B":
                rowList = [row + 1, row - 1]
                columnList = [column + 1, column - 1]
                for space in rowList:
                    if random.random() < 0.25:
                        toChange.append([space, column])
                for space in columnList:
                    if random.random() < 0.25:
                        toChange.append([row, space])
    for item in toChange:
        if item[0] >= 0 and item[0] < rows and item[1] >= 0 and item[1] < columns:
            if grid[item[0]][item[1]] == "O" or grid[item[0]][item[1]] == "R":
                grid[item[0]][item[1]] = "F"
            if grid[item[0]][item[1]] == "T":
                grid[item[0]][item[1]] = "B"

def checkRobot(grid):
    for row in grid:
        for space in row:
            if space == "R":
                return True
    return False

def prettyPrint(grid):
    print("")
    for row in grid:
        toPrint = str(row)
        toPrint = toPrint[1:]
        toPrint = toPrint[:-1]
        print(toPrint)     
        
def unexplored(space):
    if space == "O":
        return True
    else:
        return False

def safeFromFire(grid, row, column):
    if row + 1 < len(grid):
        if grid[row + 1][column] == "B" or grid[row + 1][column] == "F":
            return False
    if row - 1 >= 0:
        if grid[row - 1][column] == "B" or grid[row - 1][column] == "F":
            return False
    if column + 1 < len(grid[0]):
        if grid[row][column + 1] != "B" or grid[row][column + 1] != "F":
            return False
    if column - 1 >= 0:        
        if grid[row][column - 1] != "F" or grid[row][column - 1] != "B":
            return False
    return True

def safeFromFallingTrees(grid, row, column):
    if row + 2 < len(grid):
        if grid[row + 2][column] == "B":
            return False
    if row - 2 >= 0:
        if grid[row - 2][column] == "B":
            return False
    if column + 2 < len(grid[0]):
        if grid[row][column + 2] != "B":
            return False
    if column - 2 >= 0:        
        if grid[row][column - 2] != "B":
            return False
    return True

def notTree(space):
    if space != "T":
        return True
    else:
        return False

def inBounds(grid, row, column):
    if row < len(grid) and row >= 0 and column < len(grid[0]) and row >= 0:
        return True
    else:
        return False

def main():
    grid = generateGrid(10, 10, 0.10, 1)
    prettyPrint(grid)
    robotLocation = [0, 0]
    while checkRobot(grid):
        
        updateGrid(grid)
        prettyPrint(grid)

main()