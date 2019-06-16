def solve(fname):
    fin = open(fname, 'r')
    counter = 0 # Initialize the counter that's eventually the output
    numbers = int(fin.readline()[:-1])
    for i in range(0, numbers):
        word = fin.readline()[:-1]
        foundM = False # Reset flag
        for letter in word:
            if foundM:
                if letter.lower() == 'e': # Case insensitive matching
                    counter += 1
                    break # Save time
            else: # Case insensitive matching
                if letter.lower() == 'm':
                    foundM = True # Sets the flag that indicates an m was encountered

    print(counter) #Too lazy to format my answer for this code, do it yourself lmao
    fin.close()


for i in range(1, 6):
    solve('%d.in' % i)
