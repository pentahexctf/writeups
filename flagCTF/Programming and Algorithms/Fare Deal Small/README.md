# flagCTF – Fare Deal (Small)

* **Category:** Programming and Algorithms
* **Points:** 75

## Challenge

> The Western Milkyway Autonomous Transit Association (WMATA) is holding a promotion to attract new customers, and they need your help!
> 
> The WMATA serves N (1 <= N <= 1000) different routes, ranging in price from H (1 <= H <= 2) to K (5 <= K <= 10) Universal Standard Dollars (USD). The fare for each of the routes in this test case is an integer number.
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

This problem was much simpler than the large variant.

A simple naive solution is to enumerate through the integers between the minimum range and the maximum range. For each of the integers, divide it by every single route to determine how many trips someone can make with that much money. If the number of trips is odd for a particular route, increment a counter by one. Keep a record of the highest counter and the cost that resulted in this.

```
9;9;10;10;7
```
