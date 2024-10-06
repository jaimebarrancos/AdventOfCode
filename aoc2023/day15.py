D = open("input.txt").read()
line = list(D.split(','))


p1 = 0
for code in line:
    currentValue = 0
    for letter in code:
        currentValue += ord(letter)
        currentValue *= 17
        currentValue %= 256
    
    p1 += currentValue

print(p1)



def hash(code: str) -> int:
    
    currentValue = 0
    for letter in code:
        currentValue += ord(letter)
        currentValue *= 17
        currentValue %= 256

    return currentValue

def getFocusPower(box: int, slot:int , focal:int) -> int:
    return (box + 1) * slot * focal

def removeLens(box: int, label: str) -> None:


    for t in range(len(dix[box])):
        if label in dix[box][t]:
            dix[box].pop(t)
            break


def emptyDix() -> dict:
    d = {}
    for i in range(256):
        d[i] = []
    return d

def addLens(box: int, power: int, label: str) -> None:
    ran = False
    for t in dix[box]:
        if label in t:
            t[1] = power
            ran = True
    if ran == False:
        dix[box].append([label, power])
    
dix = emptyDix()
for text in line:

    if "=" in text:
        label = text.split("=")[0]
        box = hash(label)
        focalPower = text.split("=")[1]
        addLens(box, focalPower, label)


    elif "-" in text:
        label = text.split("-")[0]
        box = hash(label)
        removeLens(box, label)

    else:
        raise ValueError("should not be here")


p2 = 0

for box, lists in list(dix.items()):
    for index in range(len(lists)):
        x = getFocusPower(box, index + 1, int(lists[index][1]))
        
        p2 += x
print(p2)
