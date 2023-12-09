D = open("input.txt").read()
lst = list(enumerate(list(D.split('\n'))))


def getResult(isPart2):
    r = 0

    for i, line in lst:
        values = list(int(a) for a in line.split())
        if isPart2:
            values = values[::-1]
        n = 0
        cLine = values
        lineBelow = []
        totalLines = [cLine]
        flag = True
        while flag:

            if n == len(cLine) - 1: 
                totalLines.append(lineBelow)
                if all(x == 0 for x in lineBelow): break 
                cLine = lineBelow
                lineBelow = []
                n = 0

            lineBelow.append(cLine[n + 1] - cLine[n])
            n+=1

        totalLines = totalLines[::-1]
        result = [0]
        for index in range(len(totalLines)):

            result.append(result[-1] + totalLines[index][-1])
            if index == len(totalLines) - 1: 
                break
        r += result[-1]
    return r

print(getResult(False))
print(getResult(True))


# Recursive

D = open("input.txt").read()
lst = list(D.split('\n'))

def getDifference(nums):
    newL = []
    for i in range(len(nums)-1):
        newL.append(nums[i+1]- nums[i])

    if all(l == 0 for l in newL):
        return nums[-1]
    #print("number", nums[-1], "nextLine", newL)
    return nums[-1] + getDifference(newL)

p1=0
for line in lst:
    p1 += getDifference(list(map(int, line.split())))
print(p1)