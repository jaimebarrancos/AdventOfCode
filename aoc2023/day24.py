D = open("input.txt").read()
from itertools import combinations


def getEquation(line: str) -> (int, int):

    left, right = line.split("@")
    x, y ,_ = left.split(",")
    v1, v2, _ = right.split(",")

    m = int(v2) / int(v1)
    b = int(y) - m * int(x)

    print("coords", x, y, [v1, v2], m, b)
    return (m, b, (x,y), (v1,v2))


def intersectEquationsInArea(line1, line2) -> bool:
    (m1, b1, (x1,_), (vx1,_)) = line1
    (m2, b2, (x2,_), (vx2,_)) = line2

    if m1 == m2:
        return False
    
    x = (b1 - b2) / (m2 - m1)
    y = m1 * x + b1

    #return 7 < x < 27 and 7 < y < 27 and m1 * (x - int(x1)) >= 0
    return 2 * 10**14 <= x <= 4 * 10**14 and 2 * 10**14 <= y <= 4 * 10**14 and int(vx1) * (x - int(x1)) >= 0 and int(vx2) * (x - int(x2)) >= 0

#15838

def countAllIntersections1(equations:list ) -> int:
    count = 0
    for i, line1 in enumerate(equations):
        for line2 in equations[i+1:]:

            if intersectEquationsInArea(line1, line2):
                count += 1
    return count

def countAllIntersections(equations:list ) -> int:
    combs = set(combinations(equations, 2))
    count = 0

    for line1, line2 in combs:
        if intersectEquationsInArea(line1, line2):
            print(line1,line2, "\n")
            count += 1
    return count


def getEquations() -> list:
    equations = []
    for line in D.split("\n"):
          equations.append(getEquation(line))
    return equations


def p1() -> int:
    equations = getEquations()
    print(equations)
    return countAllIntersections(equations)

print(p1())