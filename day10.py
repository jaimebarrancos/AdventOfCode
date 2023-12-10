import re
import sys

sys.setrecursionlimit(40000)


D = open("input.txt").read()
lines = list(D.split('\n'))
elements = list(letter for letter in lines)

coordX = 0
coordY = 0
for line in lines:
    found = line.find("S")

    if found != -1:
        coordX += found
        break
    coordY = coordY + 1


def getNextCoords(xx, yy, direction):
    lett = lines[yy][xx]
    #print("b4 - ", lett, xx,yy, direction)

    if lett == "F":
        if direction == "up":
            direction = "right"
        elif direction == "left":
            direction = "down"
    elif lett == "7":
        if direction == "up":
            direction = "left"
        elif direction == "right":
            direction = "down"
    elif lett == "|":
        if direction == "up":
            direction = "up"
        elif direction == "down":
            direction = "down"
    elif lett == "L":
        if direction == "left":
            direction = "up"
        elif direction == "down":
            direction = "right"
    elif lett == "J":
        if direction == "down":
            direction = "left"
        elif direction == "right":
            direction = "up"
    elif lett == "-":
        if direction == "left":
            direction = "left"
        elif direction == "right":
            direction = "right"
    
    if direction == "right":
        xx += 1
    elif direction == "left":
        xx -=1
    elif direction == "down":
        yy +=1
    elif direction == "up":
        yy -=1
    #print("after - ", lett, xx,yy, direction)
    return xx,yy, direction


loopCoords = [(coordX, coordY)]

def search(x, y, dir, x2, y2, dir2):

    n = 1
    while True:
        if lines[y][x] != "-":
            loopCoords.append((x,y))
        if lines[y2][x2] != "-":
            loopCoords.append((x2,y2))

        n += 1
        a,b,c = getNextCoords(x,y, dir)
        a2,b2,c2 = getNextCoords(x2,y2, dir2)


        if (a2,b2) == (a,b) :
            loopCoords.append((a,b))
            print("LOOPIE")
            break

        x,y,dir = a,b,c
        x2,y2,dir2 = a2,b2,c2
    return n

print(search(coordX + 1, coordY, "right", coordX, coordY + 1, "down"))
#print(loopCoords)
#print(search(coordX, coordY - 1, "up", coordX, coordY + 1, "down"))

p2 = 0
for i, line in list(enumerate(lines)):

    lineCoords = []
    for coord in loopCoords:
        if coord[1] == i:
            lineCoords.append(coord)

    lineCoords = sorted(lineCoords)

    index = 0
    while index < len(lineCoords):
        if len(lineCoords) <= 1: break

        p2 += lineCoords[index + 1][0] - lineCoords[index][0] - 1
        #print(i, " - i e resto", p2, index, len(lineCoords))
        index += 2
#print(p2)

