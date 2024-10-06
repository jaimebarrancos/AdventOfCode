import re
import sys

sys.setrecursionlimit(3000)

D = open("input.txt").read().strip()
lst = enumerate(D.split('\n'))
lst = [(a,b) for a,b in lst]
p1 = 0
p2 = 0

for i,line in lst:
    d = line.split("|")
    cardPoints = 0

    #left nums
    for lNum in re.finditer(r"\d+", d[0].split(":")[1]):
        for rNum in re.finditer(r"\d+", d[1]):

            if lNum.group() == rNum.group():

                if cardPoints==0:
                    cardPoints=1
                else:
                    cardPoints*=2
    p1 += cardPoints


def countLine(i, count):
    l = [b for a,b in lst if a == i][0]
    d = l.split("|")
    cnt = 0
    #left nums
    for lNum in re.finditer(r"\d+", d[0].split(":")[1]):
        for rNum in re.finditer(r"\d+", d[1]):
            if lNum.group() == rNum.group():
                cnt += 1

    if cnt != 0:
        count += cnt
        count += sum([countLine(i + r + 1, 0) for r in range(cnt)])
        #count += sum(map(lambda r: countLine(i + r, 0), range(cnt)))
    return count

for i,line in lst:
    print(i,line)
    p2 += 1
    p2 += countLine(i,0)

print(p1)
print(p2)
