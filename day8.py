

D = open("input.txt").read()

lst = list(enumerate(list(D.split('\n'))))

lin1 = lst[0][1]
# current : Left, Right
linesDix = {}
for i, line in lst[2:]:

    a = line.split(" = ")[0]
    L = line.split(" = ")[1].split(", ")[0][1:]
    R = line.split(" = ")[1].split(", ")[1][:-1]
    linesDix[a] = (L,R)

def getNextLine(current, letter):
    if letter == "L":
        return linesDix[current][0]
    else:
        return linesDix[current][1]
    
currentLine = "AAA"
notFound = True
p1 = 0
while notFound:

    for letter in lin1:
        #print(currentLine)
        currentLine = getNextLine(currentLine, letter)
        p1 += 1
        if currentLine == "ZZZ":
            notFound = False




#######################
#### p2
ordL = ord("L")
ordA = ord("A")
def getNextLine(current, letter):
    if ord(letter) == ordL:
        return linesDix[current][0]
    else:
        return linesDix[current][1]

# linesKeys = []

# for line in linesDix:
#     if line[2] == "A":
#         linesKeys.append(line)

# print(linesKeys)
# notFound = True
# p2 = 0
# while notFound:

#     for letter in lin1:
#         for keyIndex in range(len(linesKeys)):
#             #if linesKeys[keyIndex][2] == "Z":
#             #    print("ZEE", linesKeys[keyIndex]) 
#             linesKeys[keyIndex] = getNextLine(linesKeys[keyIndex], letter)
#             #if linesKeys[keyIndex][2] == "Z":
#                 #print("ZEE", linesKeys[keyIndex]) 
#             #print(linesKeys[keyIndex])

#         p2 += 1
#         if sum(k[2] == "Z" for k in linesKeys) == len(linesKeys):
#             notFound = False
#         #print("try again", linesKeys)


# print(p2)



import functools 
linesKeys = []

for line in linesDix:
    if line[2] == "A":
        linesKeys.append(line)

print(linesKeys)
result = []
notFound = True
count = 0
for keyIndex in range(len(linesKeys)):
    while notFound:

        for letter in lin1:
            linesKeys[keyIndex] = getNextLine(linesKeys[keyIndex], letter)

            count += 1
            if linesKeys[keyIndex][2] == "Z":
                result.append(count)
                print(result)
                notFound = False
    count = 0
    notFound = True


def __gcd(a, b):
    if (a == 0):
        return b
    return __gcd(b % a, a)
 
# recursive implementation
def LcmOfArray(arr, idx):
   
    # lcm(a,b) = (a*b/gcd(a,b))
    if (idx == len(arr)-1):
        return arr[idx]
    a = arr[idx]
    b = LcmOfArray(arr, idx+1)
    return int(a*b/__gcd(a,b)) # __gcd(a,b) is inbuilt library function

        
print(p1)
print(LcmOfArray(result,0))
