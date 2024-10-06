D = open("input.txt").read()
L = D.split('\n')
import heapq


queue = []
dix = {}
for line in L:
    l,r = line.split(" -> ")

    r = r.split(", ")
    if l == "broadcaster":
        for e in r:
            heapq.heappush(queue, (e, 1))
    else: #type, list output, pulse, state
        dix[l[1:2]] = [l[0], r, 0, False]

while True:

    lst, pulse = heapq.heappop(queue)
    for e in lst:
        if dix[e][0] == "%":
            if pulse == 1:
                dix[e][2] = 1

                if dix[e][3] == False:
                    dix[e][3] = True
                    for el in dix[e][1]:
                        heapq.heappush(queue, (el, 2))
                elif dix[e][3] == True:
                    dix[e][3] = False
                    for el in dix[e][1]:
                        heapq.heappush(queue, (el, 1))
