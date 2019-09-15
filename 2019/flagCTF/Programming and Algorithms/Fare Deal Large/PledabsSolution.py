fin = open("4.in", "r")
numbers = fin.readline()[:-1].split(" ")
numbers = [int(float(i) * pow(10, 9)) for i in numbers]
minrange = numbers[1]
maxrange = numbers[2]

#print (minrange)
#print (maxrange)

total = numbers[0] / pow(10, 9)
i=0
costs = []

starts = []
ends = []

while i < total:
	x=int(float(fin.readline().split("\n")[0]) * pow(10, 9))
	costs.append(x)
	c = x
	while c < maxrange:
		starts.append(c)
		top = c + x
		if top > maxrange:
			top = maxrange
		ends.append(top)
		c += x * 2
	i += 1
	
#print (starts)
#print (ends)

n = len(starts)

max_c = 0
best_pos = -1
for i in starts:
	c = 0
	j = 0
	while j < n:
		if i >= starts[j] and (i < ends[j] or (ends[j] == maxrange and i <= ends[j])):
			c += 1
		j += 1
	if c > max_c:
		best_pos = i
		max_c = c
		
print (best_pos)