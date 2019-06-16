for i in range(1, 6):
    fin = open(str(i) + ".in", "r")

    counter = 0
    numbers = int(fin.readline()[:-1])
    for i in range(0, numbers):
        word = fin.readline()[:-1]
        foundM = False
        for letter in word:
            #print(letter)
            if foundM:
                if letter.lower() == 'e':
                    counter += 1
                    #print("Found the letter \'e\' after an occurrence of \'m\'.")
                    break
            else:
                if letter.lower() == 'm':
                    foundM = True
                    #print("Found the first occurence of \'m\'.")

    print(counter)
    fin.close()
