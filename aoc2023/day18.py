D = open("input.txt").read()
lines = list(D.split('\n'))
import heapq


def getDirCoords(letter: str) -> (int,int):
    if letter == "R":
        return (1,0)
    elif letter == "L":
        return (-1,0)
    elif letter == "U":
        return (0,-1)
    elif letter == "D":
        return (0,1)
    else: raise ValueError("got here")
    

def getAllAdj(matrix: list, x:int, y:int):
    queue = [(x,y)]
    visited = set()

    while queue:
        x,y = heapq.heappop(queue)

        matrix[y][x] = "#"
        if (x ,y) in visited:
            continue
        visited.add((x,y))

        for direction in ((1,0), (-1,0), (0,-1), (0,1)):
            newX =  x + direction[0]
            newY = y + direction[1]
            #print(x,y)
            if (newX,newY) not in vertices:
                heapq.heappush(queue, (newX, newY))

x = 0
y = 0

vertices = []

for line in lines:
    d, amt, _ = line.split()

    dir = getDirCoords(d)
    for times in range(int(amt)):
        x += dir[0]
        y += dir[1]
        vertices.append((x,y))


print(vertices)

area1, area2 = 0, 0
for i, (x, y) in enumerate(vertices):
    x2, y2 = vertices[(i + 1) % len(vertices)]
    area1 += x * y2 - x2 * y


print("part1: ", area1//2, len(vertices) // 2 + 1)
print("part1: ", area1//2 + len(vertices) // 2 + 1)
