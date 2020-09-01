# CyberClassCTF - AESthetic

* **Category:** Crypto
* **Points:** 200

## Challenge

> The snocci is looking at wall decor for the interior of her lair. You've been given a file, a key, and an IV. What's the flag?
> 
> Key: cyberclasscrypto IV: muchbigaesthetic

(aesthetic.txt was attached)

## Solution

Frankly, this challenge was disappointingly easy and, in my opinion, inflated.

It's literally just AES decoding. You're given everything you need.

After decoding, you see something that's obviously a PNG header.

The image gives you the flag.


```
cctf{a_pr3TTY_m0unta1n}
```