lis = [(40,219), (81,1012), (77,1365), (72,1089)]
p1 = 1

for t, d in lis:

    raceRecords = 0
    for secondHolding in range(t):
        dTraveled = (secondHolding * (t - secondHolding))
        if dTraveled > d:
            raceRecords += 1
    p1 = raceRecords * p1

lis = [( 40817772,219101213651089)]
p2 = 0

for t, d in lis:
    for secondHolding in range(t):
        dTraveled = (secondHolding * (t - secondHolding))
        if dTraveled > d:
            p2 += 1

print(p1)
print(p2)


# with binary search
time,record = 40817772,219101213651089


hold =  40817772
left = 0
while left < hold:
    middle = (left + hold) / 2
    dTraveled = middle * (time - middle)

    # more to the right 
    if dTraveled > record:
        left = middle + 1
    
    # more to the left 
    else :
        hold = middle


print(left,hold)
if time % 2 == 0 :
    p2 = time - ((time - hold + 1) * 2 - 1)
else :
    p2 = time - ((time - hold + 1) * 2)

print(p2)