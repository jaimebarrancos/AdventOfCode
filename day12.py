
lines = open("input.txt").read().split("\n")

processedBlocks = {}
def possibilidades(line, blocks, bi, currentSize,ind):
    key = (len(line), bi, currentSize)
    
    if key in processedBlocks:
        return processedBlocks[key]
    if line == "":
        if bi==len(blocks) and currentSize==0:
            return 1
        elif bi==len(blocks)-1 and blocks[bi]==currentSize:
            return 1
        else:
            return 0

    size = 0
    i = 0
    resto = line[i+1:]

    if line[i] in [".", "#"]:
        if line[i] =='.' and currentSize == 0:
            size += possibilidades(resto, blocks, bi, 0, ind)
        elif bi<len(blocks) and line[i] =='.' and blocks[bi]==currentSize and currentSize>0:
            size += possibilidades(resto, blocks, bi+1, 0, ind)
        elif line[i] =='#':
            size += possibilidades(resto, blocks, bi, 1 + currentSize,ind)

    elif line[i] == "?":    
        for choose in [".", "#"]:
            if choose =='.' and currentSize == 0:
                size += possibilidades(resto, blocks, bi, 0,ind)
            elif bi<len(blocks) and choose =='.' and blocks[bi]==currentSize and currentSize>0 :
                size += possibilidades(resto, blocks, bi+1, 0,ind)
            elif choose =='#':
                size += possibilidades(resto, blocks, bi, 1 + currentSize,ind)
    
    processedBlocks[key] = size
    return size

p1 = 0
for line in lines:
    lineStart = line.split()[0]
    nums = list(int(i) for i in line.split()[1].split(","))
    
    p1 += possibilidades(lineStart, nums, 0, 0)


print(p1)


p2 = 0
for line in lines:
    lineStart = line.split()[0]
    nums = list(int(i) for i in line.split()[1].split(","))
    
    lineStart = lineStart + lineStart + lineStart + lineStart+ lineStart
    nums = nums + nums + nums + nums + nums

    print(processedBlocks)
    processedBlocks.clear()
    x = possibilidades(lineStart, nums, 0, 0,0)
    p1 += x
    print(x)


print(p1)

