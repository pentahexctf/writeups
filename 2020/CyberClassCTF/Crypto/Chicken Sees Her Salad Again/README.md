# CyberClassCTF - Chicken Sees Her Salad Again

* **Category:** Crypto
* **Points:** 150

## Challenge

> Decrypt the following to find the flag: 18 18 9 21{9 23 16 9 8 22 4 9 9 16 17 20 16 22 4 4 19 8 16 1 16 19}
> 
> Note: submit in all caps.

## Solution

We quickly notice that all of the numbers are in the range 1-26.

I wonder. I really do.

After decoding it with the "alphabet cipher" or "letter numbers" or "A1Z26" or whatever the kids are calling it these days, we get a string of nonsense.

rot with n=11.


```
CCTF{THATSGOTTABEAGOODSALAD}
```