D = open("input.txt").read()
lst = list(enumerate(list(D.split('\n'))))

expanded = []
for i, l in lst:

    allPoints = True
    for let in range(len(l)):
        if l[let] != ("."):
            allPoints = False
    if allPoints:
        expanded.append(l)
    expanded.append(l)

doneCol = []
col = -1
lenn = len(expanded[0]) -1
while col < lenn:
    col += 1
    allPoints = True
    if col in doneCol:
        continue

    for line in range(len(expanded)):
        if expanded[line][col] != ("."):
            allPoints = False

    if allPoints:
        for line in range(len(expanded)):
            
            expanded[line] = expanded[line][:col] + "." + expanded[line][col:]
        doneCol.append(col +1 )
        lenn +=1


for line in expanded:
    print(line)
# galaxy x,y
coords = []
for i, l in enumerate(expanded):
    for let in range(len(l)):
        if l[let] != ("."):
            coords.append((let,i))
print(coords)

p1 = 0
b = 0
for start in range(len(coords)):
    while b != len(coords):

        
        x,y = coords[start]
        x1,y1 = coords[b]

        if b>start :

            d = abs(x1-x) + abs(y1-y)
            #print(d,"aaaaa", x, "coords B",x1,y1)
            p1 += d

        #print(i, pair)
        b += 1
    b = 0

#print(coords)

print(p1)