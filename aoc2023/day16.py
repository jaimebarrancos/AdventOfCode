import sys
sys.setrecursionlimit(3000)



D = open("input.txt").read()
lines = list(D.split('\n'))


startPos = (0,0)
direction = "r"

HEIGHT = len(lines) 
WIDTH = len(lines[0])

ENERGIZED = [[0,0,"r"]]
#ENERGIZED.append([x,y,d])

energCoords = []

p1 = 0
def move(pos: list, d:str) -> int:
    x = pos[0]
    y = pos[1]
    
    if d == "r":
        x += 1
    elif d == "l":
        x += -1
    elif d == "u":
        y += -1
    elif d == "d":
        y += 1
    
    if y < 0 or y >= HEIGHT or x < 0 or x >= WIDTH:
        return 0
    
    pos = (x,y)
    letter = lines[y][x]
    

    newDir = d
    newDir2 = ""

    if letter == ".":
        pass

    elif letter == "\\":
        if d == "r":
            newDir = "d"
        elif d == "l":
            newDir = "u"
        elif d == "u":
            newDir = "l"
        elif d == "d":
            newDir = "r"
        else:
            raise ValueError("should not get here !!")

    elif letter == "/":
        if d == "r":
            newDir = "u"
        elif d == "l":
            newDir = "d"
        elif d == "u":
            newDir = "r"
        elif d == "d":
            newDir = "l"
        else:
            raise ValueError("should not get here !!")
    
    elif letter == "-":
        if d == "r" or d =="l":
            newDir = d
        elif d == "u" or d == "d":
            newDir = "r"
            newDir2 = "l"
        else:
            raise ValueError("should not get here !!")
        
    elif letter == "|":
        if d == "r" or d == "l":
            newDir = "d"
            newDir2 = "u"
        elif d == "u" or d == "d":
            newDir = d        
        else:
            raise ValueError("should not get here !!")

    if [x,y,d] in ENERGIZED:
        return 0
    ENERGIZED.append([x,y,newDir])

    if newDir2 != "":
        move(pos, newDir)
        if [x,y,d] in ENERGIZED:
            return 0
        ENERGIZED.append([x,y,newDir2])
        move(pos, newDir2)
    else:

        move(pos, newDir)

print(move((0,0),"r"))

coords = []
for e in ENERGIZED:
    coords.append(e[:2])

print(len(coords))
l = set((i[0], i[1]) for i in coords)    
print(len(l))
#print(l)
