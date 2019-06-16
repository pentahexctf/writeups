import csv
found = [] # Initalizes the list used to store the songs
with open('Hot Stuff.csv') as fin:
    reader = csv.reader(fin)
    for row in reader:
        try:
            if int(row[1][-4:]) >= 1960 and int(row[1][-4:]) <= 2009: # Verify year, since this file goes from like 1957 to 2017
                if row[3].lower() in [i.lower() for i in row[4].split(" Featuring ")]: # Do a case insensitive comparison to the artists (including contributors)
                    found.append(row[3])
        except ValueError: # Laziness to get over the first row, which is column titles. COuld have handled this better, but whatever
            continue
found = list(dict.fromkeys(found)) # Sketchy code to get rid of duplicates - since a dictionary cannot have duplicate keys
found.sort() # We do this so that we can get the first song (alphabetically)
print(str(len(found)) + ";" + found[0]) # Formats answer
