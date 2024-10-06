D = open("input.txt").read()
lst = list(D.split('\n\n'))

previousSymetries = []


#just turn rows to columns
def checkSymetry(lines, i, i2, maxi):


    if i2 > maxi or i < 0:
        return 0
    
    #print(i, i2, lines[i], lines[i+1])
    if lines[i] == lines[i2]:
        return 1 + checkSymetry(lines, i-1, i2+1, maxi)
    
    return - 100
    
def find_smudged_mirror_position(pattern: list[str]) -> int | None:
    for i in range(1, len(pattern)):
        diff_count = 0
        for n, row in enumerate(pattern):
            if n == i and diff_count == 1:
                return i
            mirrored = i * 2 - 1 - n
            if mirrored < len(pattern):
                diff_count += sum(1 for char1, char2 in zip(row, pattern[mirrored]) if char1 != char2)
                if diff_count > 1:
                    break
    
p1 = 0
for current, block in enumerate(lst):
    lines = block.split("\n")

    #print("BLOCK;" , lines[0][0])
    # horizontal
    for i in range(len(lines) - 1):
        symetricalCount = checkSymetry(lines, i, i+1, len(lines) - 1)

        if symetricalCount >= 1 :
            lineCount = i+1
            p1 += 100 * lineCount
            previousSymetries.append((current,i, 0))
            break

    verticalLines = []
    for c in range(len(lines[0])):
        verticalLine = ""
        for i in range(len(lines)):
            verticalLine += lines[i][c]
        verticalLines.append(verticalLine)

    # vertical
    for i in range(len(verticalLines) - 1):
        symetricalCount = checkSymetry(verticalLines, i, i+1, len(verticalLines) -1 )

        if symetricalCount >= 1 :
            lineCount = i+1
            p1 += lineCount
            previousSymetries.append((current,i, 1))
            break

    verticalLines = []

print(p1)

    

print(lst)
p2 = 0
for currentB,block in enumerate(lst):
    blockCount = 0

    #bi = -1

    # while blockCount == 0:
    #     bi += 1

    #     assert(not(block[bi] != "#" and block[bi] != "."))
    #     if bi > 0:
    #         change it back before going to the next
    #         if block[bi-1] == "#":
    #             block = block[:bi-1] + "." + block[bi:]
    #         elif block[bi-1] == ".":
    #             block = block[:bi-1] + "#" + block[bi:]
    #     change
    #     if block[bi] == "#":
    #         print("-   ", block[:bi], bi)
    #         block = block[:bi] + "." + block[bi+1:]

    #     elif block[bi] == ".":
    #         block = block[:bi] + "#" + block[bi+1:]
        
        
        #print(bi, "O block esta ssim \n", block)
    pos = find_smudged_mirror_position(block)

    print(pos)
    block = block[:pos] + "." + block[pos+1:]
    lines = block.split("\n")
    # horizontal
    for i in range(len(lines) - 1):
        symetricalCount = checkSymetry(lines, i, i+1, len(lines) - 1)

        if symetricalCount >= 1 :
            if (currentB,i,0) not in previousSymetries:
                blockCount = 100 * i+1
            break

    verticalLines = []
    for c in range(len(lines[0])):
        verticalLine = ""
        for i in range(len(lines)):
            
            verticalLine += lines[i][c]
        verticalLines.append(verticalLine)

    # vertical
    for i in range(len(verticalLines) - 1):
        symetricalCount = checkSymetry(verticalLines, i, i+1, len(verticalLines) -1 )

        if symetricalCount >= 1 :
            if (currentB,i,0) not in previousSymetries:
                blockCount = i+1
            break

    verticalLines = []
    
    p2 += blockCount
    
def diagonal_flip(pattern: list[str]) -> list[str]:
    return [''.join(chars) for chars in zip(*pattern)]


print(p1)
def get_smudged_mirror_summary(pattern: list[str]):
    horizontal = find_smudged_mirror_position(pattern)
    if horizontal is not None:
        return 100 * horizontal
    return find_smudged_mirror_position(diagonal_flip(pattern))


print(sum(get_smudged_mirror_summary(pattern) for pattern in lst))
