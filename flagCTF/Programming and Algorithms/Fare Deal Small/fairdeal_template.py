finalAnswer = [] # List so we can format our answer
for i in range(1, 6):
    fin = open(str(i) + ".in", "r")
    costs = [] # List to store the costs for each route
    numbers = fin.readline()[:-1].split(" ")
    numbers = [int(i) for i in numbers]
    minrange = numbers[1]
    maxrange = numbers[2]
    for i in range(0, numbers[0]): # Iterates through the rest of the lines, adding the costs to the list
        costs.append(int(fin.readline()[:-1]))

    oldcounter = 0 # Used so we can determine when the counter "hits a record"
    for i in range(minrange, maxrange + 1): # Iterate through the integers between the minimum cost and maximum cost
        counter = 0
        for j in costs:
            if (i//j)%2 == 1: # Check if the number of possible trips is odd
                counter += 1
        if counter >= oldcounter: # We "hit a record" - change oldcounter
            oldcounter = counter
            minrange = i # This is our answer
    finalAnswer.append(str(minrange)) # Add this to the array
    fin.close()
print(';'.join(finalAnswer)) # Format our answer
