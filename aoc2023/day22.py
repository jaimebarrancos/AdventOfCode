


def emptyMatrix(n:int) -> list:
    matrix = []
    for _ in range(n):
        plane = []
        for _ in range(n):
            row = []
            for _ in range(n):
                row.append(" ")
            plane.append(row)
        matrix.append(plane)
    return matrix

#bricks = [planes]
#planes = [rows]

# 

def getSnapshot(file) -> list:
    lines = file.split(("\n"))
    bricks = emptyMatrix(10)
    print(bricks)
    for brick in lines:
        l, r = brick.split("~")
        start = (int(i) for i in l.split(","))
        end = (int(i) for i in r.split(","))

        for pair in zip(start, end):
            if pair[0] != pair[1]:
                for cube in range(pair[0], pair[1], 1):
                    bricks[start[2]][start[1]][start[0]]
    
file = open("input.txt").read()
getSnapshot(file)