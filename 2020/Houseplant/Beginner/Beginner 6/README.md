# Houseplant CTF - Beginner 6

* **Category:** Beginner
* **Points:** 25

## Challenge

> i'm so tired...
> 
> 
> 26 26 26 26 26 26 26 26 19 12 5 5 16 9 14 7 9 14 16 8 25 19 9 3 19
> 
> 
> *disclaimer: DON'T DO THIS KIDS. only sleep in math.
> 
> Remember to wrap the whole thing in the flag format rtcp{}
> 
> Hint! this isn't a hint; this is just us expressing our regret for taking 8AM physics

## Solution

I'm going to do an actually honest writeup (with no sarcasm this time) because I'm bored and writeups are boring.

We immediately notices that all the numbers are within the range 9-26. 26 is coincidentally the number of letters in the alphabet. Our immediate thought is A1Z26, also known as "letter numbers".


```
rtcp{zzzzzzzzsleepinginphysics}
```