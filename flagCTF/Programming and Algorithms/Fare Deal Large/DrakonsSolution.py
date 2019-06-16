import math

finalAnswer = []
for i in range(1, 6):
    fin = open(str(i) + ".in", "r")
    numbers = fin.readline()[:-1].split(" ")
    numbers = [float(i) for i in numbers]
    minrange = numbers[1]
    maxrange = numbers[2]
    total = int(numbers[0])

    costs = []
    startInt = []
    endInt = []
    counter = 0
    oldcounter = 0

    for i in range(0, total):
        costs.append(float(fin.readline()[:-1]))

    for i in costs:
        sDiv = math.floor(i/maxrange)
        lDiv = math.ceil(i/minrange)
        if sDiv % 2 == 0:
            sDiv += 1
        if lDiv % 2 == 0:
            lDiv -=1
        for j in range(sDiv, lDiv + 2, 2):
            startInt.append(i * j)
            endInt.append(i * (j + 1))
    for i in startInt:
        if i < minrange:
            startInt.remove(i)
            startInt.append(minrange)
    for i in endInt:
        if i > maxrange:
            endInt.remove(i)
            endInt.append(maxrange)
    startInt.sort()
    endInt.sort()
    #print(startInt, endInt)
    
    while endInt:
        try:
            if startInt[0] < endInt[0]:
                counter += 1
                #print("Another start.")
                #print(counter)
                if counter > oldcounter:
                    oldcounter = counter
                    answer = startInt[0]
                del startInt[0]
            else:
                #print("Another end")
                #print(counter)
                counter -= 1
                del endInt[0]
        except IndexError:
            #print("Breaking")
            break
    print(answer)
    finalAnswer.append(str(answer))
print(';'.join(finalAnswer))
