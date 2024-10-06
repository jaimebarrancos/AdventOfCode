

def getMatrix(file):
    L = file.split('\n')
    matrix = []
    for line in L:
        row = []
        for letter in line:
            if letter =="S":
                row.append(".")
            else:row.append(letter)
        matrix.append(row)
    return matrix


def getAdjDot(x:int, y:int, matrix:list) -> list:
    adj = []
    for dir in ((1,0), (0,1), (-1,0), (0,-1)):
        xx = x + dir[0]
        yy = y + dir[1]

        if len(matrix[0]) - 1 < xx or xx < 0 or 0 > yy or yy > len(matrix) - 1:
            continue
        if matrix[yy][xx] == ".":
            adj.append((xx, yy))
    return adj


def step(matrix:list, plots:list) -> (list, list):
    newPlots = []
    for plot in plots:
        for adj in getAdjDot(plot[0], plot[1], matrix):
            matrix[adj[1]][adj[0]] = "O"
            newPlots.append((adj[0], adj[1]))
        matrix[plot[1]][plot[0]] = "."
    for plot in plots:
        plots.remove(plot)
    return matrix, newPlots




def step(matrix:list, plots:list) -> (list, list):
    newPlots = []
    for plot in plots:
        for adj in getAdjDot(plot[0], plot[1], matrix):
            matrix[adj[1]][adj[0]] = "O"
            newPlots.append((adj[0], adj[1]))
        matrix[plot[1]][plot[0]] = "."
    for plot in plots:
        plots.remove(plot)
    return matrix, newPlots



def isRock(x:int, y:int, matrix:list) -> bool:
    mainX = abs(x % ROWLEN)
    mainY = abs(y % COLLEN)

    return matrix[mainY][mainX] == "#"


def getAdjDot2(x:int, y:int, matrix:list) -> set:
    adj = set()
    for dir in ((1,0), (0,1), (-1,0), (0,-1)):
        xx = x + dir[0]
        yy = y + dir[1]

        if not isRock(xx, yy, matrix):
            adj.add((xx, yy))
    return adj


def step2(matrix:list, plots:set) -> (list, set):
    newPlots = set()
    
    for plot in plots:
        for adj in getAdjDot2(plot[0], plot[1], matrix):
            newPlots.add((adj[0], adj[1]))
            
    return matrix, newPlots


D = open("input.txt").read()
matrix = getMatrix(D)
plots= set(((5,5),))
ROWLEN = len(matrix[0])
COLLEN = len(matrix)


for _ in range(64):
    matrix, plots = step(matrix, plots)
    print(matrix)
print("p1", len(plots))


# works but is very slow
for _ in range(500):
    matrix, plots = step2(matrix, plots)

print(len(plots))