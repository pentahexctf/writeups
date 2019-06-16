# flagCTF – Fare Deal (Large)

* **Category:** Programming and Algorithms
* **Points:** 75

## Challenge

> Note that this is the same as "Fare Deal (Small)" except for the second paragraph of the challenge below.
> 
> The Western Milkyway Autonomous Transit Association (WMATA) is holding a promotion to attract new customers, and they need your help!
> 
> The WMATA serves N (1 <= N <= 100000) different routes, ranging in price from H (1 <= H <= 2) to K (5 <= K <= 10) Universal Standard Dollars (USD). USD allows up to 9 digits after the decimal point. Note that floating-point decimal types in most languages may not provide enough resolution to represent numbers in this problem accurately.
> 
> They will be giving away free passes loaded with T USD (H <= T <= K) in an attempt to get people hooked on the system. They know that most of their target customers take one route round-trip frequently, and customers only look to see if they have a sufficient amount on their card without seeing whether they have enough for any future return trip!
> 
> They would like customers to have to reload their pass in order to return at some point; namely they would like for the pass to be valid for a full odd number of 1-way trips. They would like this to be true for as many routes as possible, and if there are multiple ways to do this, to load the least amount on the free passes. Having less than the fare for a trip on their pass does not benefit the rider in any way.
> 
> They have hired you to determine the value of T!
> 
> Input:
> 
> Line 1 contains N, H, and K, separated by spaces.
> 
> Lines 2..N+1 contain the cost of one of the WMATA routes.
> 
> Output:
> 
> The value of T in simplest form (without unnecessary decimal points or 0s at the end).
> 
> Sample Input: 3 1 10
> 
> 3
> 
> 5
> 
> 7
> 
> Sample Input Description:
> 
> WMATA runs 3 routes, with costs of 3, 5, and 7 USD.
> 
> Sample Output:
> 
> 9
> 
> Sample Output Description: Any pass value in [9, 10), that is, of at least 9 and less than 10, gives 3 rides on the first route, 1 on the second, and 1 on the third. Out of all of these, the minimum value is 9. In this case, no matter what route the riders take, they will end up loading their pass for a return trip!
> 
> Flag Format: The output of all of the programs, without whitespace or newlines, concatenated together while separated by semicolons. For example "3;5.4321;7.8;9.129804594;4.2458".

## Solution

I'm sorry

```
# get file input
fin = open("1.in", "r")
# get first line, no newline
numbers = fin.readline()[:-1].split(" ")
# get numbers and multiply by 10^9
# n,h,k (n is integer, h and k are floating points with up to 9 decimals, want to store as int though)
numbers = [int(float(i) * pow(10, 9)) for i in numbers]
# get h,k
minrange = numbers[1]
maxrange = numbers[2]

# get n, divide by the 10^9 factor since it was an int before
total = numbers[0] / pow(10, 9)

# variable for loop
i=0

# two arrays to hold the ranges (should have used a better data type)
# starts[i] and ends[i] correspond to a range of values that makes the requested
# odd number of routes
starts = []
ends = []

# loop through each of total (n) costs
while i < total:
  # get the number, get rid of decimal by multiplying by 10^9
  x=int(float(fin.readline().split("\n")[0]) * pow(10, 9))
  # new variable to increment (don't modify x)
  c = x
  # go through odd ranges (x to 2x, 3x to 4x, and so on)
  while c < maxrange:
    # start of range (closed, does include this value in range)
    starts.append(c)
    # end of range (open, does not include this value in range)
    top = c + x
    # cap range at max range (closed, does include this value in range)
    if top > maxrange:
      top = maxrange
    # add this value at end
    ends.append(top)
    # go to next odd (think 1,3,5 -> increment by 2x)
    c += x * 2
  # this is literally a for loop but i didn't want to use range because memory, and that's slow
  i += 1

# we are looping through the starting point in each range, this is the lowest unique value
# for each point, go through each of the range and record how many times it is in the range
# aka how many times it has an odd number of routes for the price

# calculate this once because we will loop a lot
# this is going to be O(n^2) which is horrid but 10^5 is actually small for maximum n so that's okay
n = len(starts)

# store the best number
max_c = 0
# store the associated best price, -1 is just a default small value (will definitely change)
best_pos = -1

# loop through each starting value in range
for i in starts:
  # counter of routes in range
  c = 0
  # loop through ranges
  j = 0
  while j < n:
    # just checking if in range
    # end is < unless it is at endpoint, in which its <= (see notes on closed/open)
    if i >= starts[j] and (i < ends[j] or (ends[j] == maxrange and i <= ends[j])):
      c += 1
    j += 1
  # wow! we found a new best price!
  if c > max_c:
    # update prices
    best_pos = i
    max_c = c
# by the end, we have secured easy win
print (best_pos)
```

```
9;7.450588233;9.997544599;9.99970026;8.599645879
```
