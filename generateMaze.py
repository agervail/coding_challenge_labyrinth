# Maze indicices
#     x
#     *------------>
#   y |
#     |
#     |
#     |
#     v
import random

labSize = 5
width  = labSize
height = labSize
maze = {} # N : New, I : In, F : Frontier
unvisitedCells = []
inTheMazeCells = []
frontierCells  = []

def toStrMatrix(width, height, maze):
    str_matrix = [['O'] * (width * 2 + 1)
                  for i in range(height * 2 + 1)]

    for cell in maze:
        x = cell[0] * 2 + 1
        y = cell[1] * 2 + 1
        str_matrix[y][x] = ' '
        if 'N' not in maze[cell] and y > 0:
            str_matrix[y - 1][x + 0] = ' '
        if 'S' not in maze[cell] and y + 1 < height:
            str_matrix[y + 1][x + 0] = ' '
        if 'W' not in maze[cell] and x > 0:
            str_matrix[y][x - 1] = ' '
        if 'E' not in maze[cell] and x + 1 < width:
            str_matrix[y][x + 1] = ' '

    return str_matrix

def getNeighbors(width, height, cell):
    neighbors = []
    x = cell[0]
    y = cell[1]
    if x > 0:
        neighbors.append((x-1, y))
    if x < width - 1:
        neighbors.append((x+1, y))
    if y > 0:
        neighbors.append((x, y-1))
    if y < height - 1:
        neighbors.append((x, y+1))
    return neighbors

def getConnectionBetweenCells(c1, c2):
    if c1[0] < c2[0]:
        return "E", "W"
    elif c1[0] > c2[0]:
        return "W", "E"
    elif c1[1] < c2[1]:
        return "S", "N"
    elif c1[1] > c2[1]:
        return "N", "S"

for x in range(width):
    for y in range(height):
        maze[(x,y)] = []
        unvisitedCells.append((x,y))

#First we had one cell to the maze and find her neighbors and mark them as frontier
randomUnvisitedCell = (random.randint(0, width - 1), random.randint(0, height - 1))
#unvisitedCells.remove(randomUnvisitedCell)
inTheMazeCells.append(randomUnvisitedCell)
frontierCells = getNeighbors(width, height, randomUnvisitedCell)

while len(inTheMazeCells) < width * height:
    # print("inTheMazeCells : ", inTheMazeCells)
    # print("frontierCells : ", frontierCells)
    randomFrontierCell = random.choice(frontierCells)
    inTheMazeCells.append(randomFrontierCell)
    selectedCellNeighbors = getNeighbors(width, height, randomFrontierCell)
    # Select a cell that is visited and near the selected frontier currently selected
    # print("randomFrontierCell", randomFrontierCell)
    # print(selectedCellNeighbors)
    # print([visitedNear for visitedNear in selectedCellNeighbors if visitedNear in inTheMazeCells])
    visitedCellNear = random.choice([visitedNear for visitedNear in selectedCellNeighbors if visitedNear in inTheMazeCells])
    frontierWay, visitedWay = getConnectionBetweenCells(randomFrontierCell, visitedCellNear)
    maze[randomFrontierCell].append(frontierWay)
    maze[visitedCellNear].append(visitedWay)
    # print("maze", maze)

    frontierCells.remove(randomFrontierCell)
    selectedCellNeighbors = getNeighbors(width, height, randomFrontierCell)
    for neighbor in selectedCellNeighbors:
        if not neighbor in frontierCells and not neighbor in inTheMazeCells:
            frontierCells.append(neighbor)

print(maze)

print('var thing = {', end='')
for item in maze:
    print('"', item[0], ',', item[1], '"', ' : [', end='', sep='')
    for way in maze[item]:
        print('"', way, '"', ',', end='', sep='')
    print('],', end='')
print('};')
