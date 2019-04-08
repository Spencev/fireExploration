import random

def genGrid(width, height, treeDensity, fireSources):
    grid = []
    for row in range(0, height):
        rowHold = []
        for column in range(0, width):
            if random.random() < treeDensity:
                rowHold.append("T")
            else:
                rowHold.append("O")
        grid.append(rowHold)
    return grid

def prettyPrint(grid):
    for row in grid:
        toPrint = str(row)
        toPrint = toPrint[1:]
        toPrint = toPrint[:-1]
        print(toPrint)     

def main():
    grid = genGrid(15, 20, 0.50, 2)
    prettyPrint(grid)

main()