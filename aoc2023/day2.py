maxred = 12
maxgreen = 13
maxblue = 14
def createDicGame(game_str):
    sets = game_str.split(';')
    setNum = len(sets)
    gameID = int(sets[0].split(':')[0].split()[1])
    gameDic = {'Id': gameID} 
    sets[0]= sets[0][6+len(str(gameID)):]

    for i in range(setNum):
        redCount = greenCount = blueCount = 0
        colorInfo = sets[i].split(',')
        for k in range(len(colorInfo)):
            colorInfo[k] = colorInfo[k].strip()
            if 'red' in colorInfo[k]:
                redCount = int(colorInfo[k].split()[0])
            if 'green' in colorInfo[k]:
                greenCount = int(colorInfo[k].split()[0])
            if 'blue' in colorInfo[k]:
                blueCount = int(colorInfo[k].split()[0])

        gameDic[f"set{i+1}"] = {'red': redCount, 'green':greenCount, 'blue':blueCount}
    return gameDic

def IsValid(dicGame):
    for setkey, setValue in dicGame.items():
        if ('set') in setkey:
            redtoCompare = setValue['red']
            if redtoCompare > maxred:
                return False
            greentoCompare = setValue['green']
            if greentoCompare > maxgreen:
                return False
            bluetoCompare = setValue['blue']
            if bluetoCompare > maxblue:
                return False
    return True

def cubeCount(fich):

    with open(fich, 'r') as file:
        game_str = file.readline()
        countID = 0
        while game_str != '':
            dicGame = createDicGame(game_str)
            if IsValid(dicGame):
                countID += dicGame['Id']
            game_str = file.readline()
    return countID

print(cubeCount('src/input.txt'))