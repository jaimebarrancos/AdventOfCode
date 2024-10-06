import re

D = open("input.txt").read()
lst = re.findall(r"(.*?)\n\n", D, re.DOTALL)
nextOrigin = []

for i, block in enumerate(lst):
    if i == 0:
        seeds = block.split(": ")[1].split()
        seeds = [int(seed) for seed in seeds]
    else:
        if block == lst[-1]: break
        #dest, start, range
        values = [[int(value) for value in line.split()] for line in block.split(":\n")[1].split("\n")]
        values2 = [[int(value) for value in line.split()] for line in lst[i+1].split(":\n")[1].split("\n")]

        m = []
        for valueList in values:
            for row in values2:
                for i in range(valueList[2]):
                    if row[1] <= valueList[0] + i <= row[1] + row[2] and valueList[0] + i in nextOrigin:
                        m.append(valueList[0] + i)
        nextOrigin = []
        #compara destino origem 2a linha
        for row in values2:
            for val in range(row[2]):
                for ma in m:
                    nextOrigin.append(ma + val)



D = open("input.txt").read()
lst = re.findall(r"(.*?)\n\n", D, re.DOTALL)
nextOrigin = []
result = []

for i, block in enumerate(lst):
    if i == 0:
        seeds = block.split(": ")[1].split()
        seeds = [int(seed) for seed in seeds]

    elif i == 1:
        values = [[int(value) for value in line.split()] for line in block.split(":\n")[1].split("\n")]
        for seed in seeds:
            for row in values:
                for i in range(row[2]):
                    if row[1] <= seed <= row[1] + row[2]:
                        nextOrigin.append(row[0] + i) 

    elif block == lst[-1]:
        values = [[int(value) for value in line.split()] for line in block.split(":\n")[1].split("\n")]
        for row in values:
            for val in range(row[2]):
                for ma in nextOrigin:
                    result.append(ma + val)
        print("acabou")

    else:
        
        #dest, start, range
        values = [[int(value) for value in line.split()] for line in block.split(":\n")[1].split("\n")]
        values2 = [[int(value) for value in line.split()] for line in lst[i+1].split(":\n")[1].split("\n")]

        m = []
        for valueList in values:
            for row in values2:
                for i in range(row[2]):
                    for b in range(valueList[2]):
                        if valueList[0] + b == row[1] + i and row[0] + i in nextOrigin:
                            m.append(row[0] + i)
        print(nextOrigin)
        nextOrigin = []
        #compara destino origem 2a linha
        for row in values2:
            for val in range(row[2]):
                for ma in m:
                    nextOrigin.append(ma + val)
        print("2", nextOrigin)




print("result", min(result))

        
