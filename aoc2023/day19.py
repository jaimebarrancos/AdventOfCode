D = open("input.txt").read()
linesA = list(D.split('\n\n'))[0]
linesB = list(D.split('\n\n'))[1]


dix = {}
for line in linesA.split('\n'):
    if line == "" : continue
    line = line.split("{")
    name = line[0]
    content = line[1][:-1]
    attr = content.split(",")

    part = ""
    dix[name] = ()
    for i in range(len(attr)):
        if i == len(attr) - 1:
            part = attr[i]
            dix[name] += (part,)
        else:
            condition, part = attr[i].split(":")
            dix[name] += ((condition,part),)
print(dix)

def acceptedPart(x,m,a,s) -> bool:

    queue = ["in"]

    while True:
        for name in queue:
            if name == "A": return True
            elif name == "R": return False
            options = dix[name]
            queue.remove(name)
            foundElement = False

            for cond in options[:-1]:
                for letter in [("x",x),("m",m),("a",a),("s",s)]:
                    if cond[0][0] == letter[0]:
                        if queue == []:
                            if cond[0][1] == "<":
                                if letter[1] < int(cond[0][2:]):
                                    foundElement = True
                                    queue.append(cond[1])
                            elif cond[0][1] == ">":
                                if letter[1] > int(cond[0][2:]):
                                    foundElement = True
                                    queue.append(cond[1])
            if not foundElement: queue.append(options[-1])
        print(queue)



p1 = 0
for line in linesB.split('\n'):
    x,m,a,s = list(int(l.split("=")[1]) for l in line[1:-1].split(","))
    print(x,m,a,s)
    if acceptedPart(x,m,a,s):
        p1 += x+m+a+s
print(p1)
