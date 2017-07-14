from __future__ import print_function
import math
import operator

X = 'X'
S = 'S'
E = 'E'
O = 'O'

GRID = ( \
    (X, X, X, X, E, X), \
    (S, O, O, X, O, X), \
    (X, O, O, O, O, X), \
    (X, X, O, X, O, X), \
    (X, O, O, O, O, X), \
    (X, O, O, X, O, X), \
    (X, X, X, X, X, X), \
)

SIZE = (len(GRID), len(GRID[0]))

MOVES = ( \
    (0, -1), \
    (1, 0), \
    (0, 1), \
    (-1, 0), \
)

Visited = [map(lambda item: item == X, row) for row in GRID]

def getNewPos(curPos, move):
    return map(operator.add, curPos, move)

def isValidMove(curPos, move):
    newPos = getNewPos(curPos, move)
    y = newPos[0]
    x = newPos[1]
    return (0 <= x < SIZE[1]) and (0 <= y < SIZE[0]) \
            and not Visited[y][x] and GRID[y][x] != X


Steps = [[float('inf') for i in range(SIZE[1])] for j in range(SIZE[0])]

startPos = (1, 0)
Steps[startPos[0]][startPos[1]] = 0
LastPos = [[None for i in range(SIZE[1])] for j in range(SIZE[0])]


posQueue = [startPos]

def explore(curPos):
    curSteps = Steps[curPos[0]][curPos[1]]
    Visited[curPos[0]][curPos[1]] = True

    for m in MOVES:
        if isValidMove(curPos, m):
            newPos = getNewPos(curPos, m)
            posQueue.append(newPos)
            if Steps[newPos[0]][newPos[1]] > (curSteps + 1):
                Steps[newPos[0]][newPos[1]] = curSteps + 1
                LastPos[newPos[0]][newPos[1]] = curPos

while len(posQueue) > 0:
    explore(posQueue.pop(0))

for row in Steps:
    for item in row:
        if (math.isinf(item)):
            print('  X', end='')
        else:
            print('{:3}'.format(item), end='')
    print()

for row in LastPos:
    for item in row:
        print('{:6}'.format(item), end='')
    print()
