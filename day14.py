
def calculateWeight(matrix: list) -> int:
    weight = 0
    
    for column in matrix:
        countList = []

        for i in range(len(column)):
            if column[i] == "O":
                countList.append(0)
            if len(countList) != 0:
                for index in range(len(countList)):
                    countList[index] += 1
        weight += sum(countList)
    return weight


def rotate(matrix: list) -> list:
  width = len(matrix)
  height = len(matrix[0])
  newmatrix = [['?' for _ in range(width)] for _ in range(height)]
  for r in range(width):
    for c in range(height):
      newmatrix[c][width-1-r] = matrix[r][c]
  return newmatrix


def slideWest(matrix: list) -> list:

    for columnI in range(len(matrix)):
        freeSpace = 0

        for i in range(len(matrix[0])):
            if matrix[columnI][i] == "#":
                freeSpace = 0
            elif matrix[columnI][i] == ".":
                freeSpace += 1
            elif matrix[columnI][i] == "O":
                if freeSpace > 0:
                    matrix[columnI][i - freeSpace] = "O"
                    matrix[columnI][i] = "."
    return matrix


# def score(G):
#   ans = 0
#   R = len(G)
#   C = len(G[0])
#   for r in range(R):
#     for c in range(C):
#       if G[r][c]=='O':
#         ans += len(G)-r
#   return ans

def getMatrix():
    D = open("input.txt").read()
    lines = list(D.split('\n'))
    matrix = []
    for line in lines:
        matrix.append(line)

    return matrix


p1 = 0
for times in range(1):
    matrix = getMatrix()

    newmatrix = []
    for ci in range(len(matrix[0])):
        r = []
        for row in matrix:
            r.append(row[ci])
        newmatrix.append(r)

    print(slideWest(newmatrix))
    p1 += calculateWeight(newmatrix)

print(p1)



#p1 = 0
for times in range(1):
    
    #print(NumsList)
    
    #print(rotate(NumsList))
    #print(slideWest(NumsList))
    #
    # p1 += calculateWeight(NumsList)
    pass