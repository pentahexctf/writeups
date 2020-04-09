# TG:Hack 2020 – Is This The One? Or Zero?

* **Category:** n00b
* **Points:** 58

## Challenge

> Help me decrypt this, it's important for `gaia`!
> ``00110011 00100110 01011011 01010001 00011100 00001110
00000111 00000100 00111000 00001110 00011011 00111110
00011101 00000100 00011011 00001110 00111000 00000011
00011100 00010101 00111000 00001111 00000110 00010101
00111000 00000011 00000110 00010101 00001111 00011100``

## Solution

Decoding from binary, this looks like garbage data. My first thought is XOR, and I assume the plaintext is the flag, so I crib drag.
The key appears to be `gaia`. It's at this point that I realize that the key was in the challenge description. Whoops.

We XOR with the key `gaia` and get the flag.

```
TG20{one_or_zero_but_not_both}
```