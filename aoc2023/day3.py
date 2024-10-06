
numbers = "1234567890"
D = open("input.txt").read().strip()
sum = 0
gearRatioSum = 0

previousIndexes = {}
numIndexes = {}
lineCounter = 0

symbolDix = {}

for line in D.split('\n'):

    characterCounter = 0
    # {index: line}
    for wordOrSymbol in line.split("."):
        currentNumber = ""

        # {[numIndex, line]: number }
        numI = ()
        if wordOrSymbol != "":
            characterCounter += 1
            for digitIndex in range(len(wordOrSymbol)):

                #if number is starting
                if wordOrSymbol[digitIndex] in numbers:

                    currentNumber += wordOrSymbol[digitIndex]
                    numI += (characterCounter,)

                # is symbol
                else :
                    previousIndexes[(characterCounter, lineCounter)] = wordOrSymbol[digitIndex]
                    if currentNumber != "":
                        numIndexes[(numI, lineCounter)] = currentNumber
                        currentNumber = ""
                        numI = ()
                        
                characterCounter += 1
            numIndexes[(numI, lineCounter)] = currentNumber
            numI = []
        else :
            characterCounter += 1
    lineCounter += 1

# if there is a symbol adjacent
alreadyCounted = []
for numIndex, line in numIndexes:

    for i, lineC in previousIndexes:
        #print(numIndex)
        for number in numIndex:
            #print(number, lineC)
            if line == lineC + 1 or line == lineC or line == lineC - 1:

                if max(numIndex) + 1 >= i >= min(numIndex) - 1:
                    if (numIndex, line) not in alreadyCounted:
                        if previousIndexes[i, lineC] == "*":
                            if (i, lineC) not in symbolDix:
                                symbolDix[i, lineC] = [numIndexes[(numIndex, line)]]
                            elif len(symbolDix[i, lineC]) == 1:
                                symbolDix[i, lineC].append(numIndexes[(numIndex, line)])

                        alreadyCounted.append((numIndex, line))
                        sum += int(numIndexes[(numIndex, line)])

for symbol, numList in symbolDix.items():
    if len(numList) == 2:
        gearRatioSum += int(numList[0]) * int(numList[1])

print(sum)
print(gearRatioSum)