D = open("input.txt").read()
lst = list(D.split('\n'))


ORDERS = reversed('AKQJT987654321')
ORDER = {v: k for k, v in enumerate(ORDERS)}

def orderB(arg):
    st = arg[1].split()[0]
    
    return st

    # is start of string equal?
    # if so compare rest of string
    # b = 0
    # for a in range(len(st)):
    #     if a == len(st) - 1: break
    #     if st[a] != st[a + 1]:
    #         b = a
    #         return ord(st[b])
    
orde = list(enumerate(sorted(lst, key=lambda x: x[1].split()[0], reverse=True)))
def getLetters(line):
    for l, card in orde:
        if l == line:
            card = card.split()[0]
            order = []
            for letter in card:
                order.append(ORDER[letter])
            print(order)
            return order
        
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

#print(allDix)
lineTypes = {}
for i, diction in list(allDix.items()):
    secondBiggestNum = 0
    my_keys = sorted(diction, key=diction.get, reverse=True)
    my_values = list(diction[k] for k in my_keys)[:2]

    #for a,b in list(diction.items()): # []
        # if b > secondBiggestNum:
        #     if b > biggestNum:
        #         biggestNum = b
        #     else :
        #         secondBiggestNum = b
    if len(my_values) == 1:
        my_values = [5,0]
    lineTypes[i] = my_values


r = sorted(lineTypes.items(), key=lambda x:(-x[1][0], -x[1][1], getLetters(x[0])))

di = dict(orde)
#print("original",di)
#print("R", r)
sum = 0
n = 5
for card in r:
    bid = int(di[card[0]].split()[1])

    #print(bid,n)
    win = bid * n
    sum += win
    n -= 1


print("result", sum)
