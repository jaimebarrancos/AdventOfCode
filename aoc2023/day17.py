
import heapq

D = open("input.txt").read()
lines = list(D.split('\n'))



def dijkstra(matrix):
    maxR = len(matrix)
    maxC = len(matrix[0])

    #heat, coords, direction, count to 3
    queue = [(0,0,0,0,0,0)]

    visited = set()
    while queue:

        heat, x, y, dirX, dirY, count = heapq.heappop(queue)
        if x == maxC - 1 and y == maxR - 1:
            print("p1", heat)
            break

        if (x, y, dirX, dirY, count) in visited:
            continue

        visited.add((x, y, dirX, dirY, count))

        # se for mesma direcao
        if count < 3 and (dirX,dirY) != (0,0):
            
            newX = x + dirX
            newY = y + dirY

            if newX >= 0 and newX < maxC and newY >= 0 and newY < maxR:
                heapq.heappush(queue, (heat + matrix[newX][newY], newX, newY, dirX, dirY, count + 1))


        # mudar direção
        for k in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if (-dirX,-dirY) != k and (dirX,dirY) != k:

                newX = x + k[0]
                newY = y + k[1]

                if newX >= 0 and newX < maxC and newY >= 0 and newY < maxR:
                    heapq.heappush(queue, (heat + matrix[newX][newY], newX, newY, k[0], k[1], 1))





matrix = []

for line in lines:
    row = []
    for e in line:
        row.append(int(e))
    matrix.append(row)

dijkstra(matrix)





def dijkstra2(matrix):
    maxR = len(matrix)
    maxC = len(matrix[0])

    #heat, coords, direction, count to 3
    queue = [(0,0,0,0,0,0)]

    visited = set()
    while queue:

        heat, x, y, dirX, dirY, count = heapq.heappop(queue)
        if x == maxC - 1 and y == maxR - 1 and count > 3:
            print("p2", heat)
            break

        if (x, y, dirX, dirY, count) in visited:
            continue

        visited.add((x, y, dirX, dirY, count))

        # se for mesma direcao
        if count < 10 and (dirX,dirY) != (0,0):
            
            newX = x + dirX
            newY = y + dirY

            if newX >= 0 and newX < maxC and newY >= 0 and newY < maxR:
                heapq.heappush(queue, (heat + matrix[newX][newY], newX, newY, dirX, dirY, count + 1))


        # mudar direção
        if count > 3 or (dirX, dirY) == (0, 0):
            for k in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if (-dirX,-dirY) != k and (dirX,dirY) != k:

                    newX = x + k[0]
                    newY = y + k[1]

                    if newX >= 0 and newX < maxC and newY >= 0 and newY < maxR:
                        heapq.heappush(queue, (heat + matrix[newX][newY], newX, newY, k[0], k[1], 1))



dijkstra2(matrix)
