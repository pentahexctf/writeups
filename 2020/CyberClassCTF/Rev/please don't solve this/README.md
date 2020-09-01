# CyberClassCTF - please don't solve this!

* **Category:** Rev
* **Points:** 200

## Challenge

> Please don't crack my amazing password encrypter and figure out the password!
> 
> Part 1/2

(Main.java was attached)

## Solution

The encrypt() function goes through each character. If the charcode is even, it adds 2, and if the charcode is odd, it subtracts 2.

Since it is adding/subtracting 2, parity is conserved. Therefore, we can go through each character in the ciphertext and add/subtract accordingly.

```
cctf{n3v3r_g0nna_g1v3_y0u_up}
```