D = open("input.txt").read()
lst = list(D.split('\n'))

def orderB(arg):
    st = arg[1].split()[0]
    return st
    # is start of string equal?
    # if so compare rest of string
    #b = 0
    # for a in range(len(st)):
    #     if a == len(st) - 1: break
    #     if st[a] != st[a + 1]:
    #         b = a
    #         return ord(st[b])
orde = list(enumerate(sorted(lst, key=lambda x: x[1].split()[0], reverse=True)))
              
allDix = {}
for i, line in orde:
    card, bid = line.split()


    dix = {}
    for letter in card:
        if letter in dix:
            dix[letter] += 1
        else:
            dix[letter] = 1
    allDix[i] = dix

lineTypes = {}
for i, d in list(allDix.items()):
    biggestNum = 1
    secondBiggestNum = 1
    for a,b in list(d.items()):
        if b > secondBiggestNum:
            if b > biggestNum:
                biggestNum = b
            else :
                secondBiggestNum = b
    lineTypes[i] = [biggestNum, secondBiggestNum]


r = sorted(lineTypes.items(), key=lambda x:(x[1][0], x[1][1], -x[0]))

di = dict(orde)
print("original",di)
print("R", r)
sum = 0
n = 1
for card in r:
    bid = int(di[card[0]].split()[1])

    print(bid,n)
    win = bid * n
    sum += win
    n += 1



print("result", sum)
        #get type and compare with others
        #if b == 5: