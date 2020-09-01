# CyberClassCTF - WHY WOULD YOU SOLVE THIS!

* **Category:** Rev
* **Points:** 500

## Challenge

> I have improved my password encrypting algorithm! I bet you can't get my password now!!!!!!
> 
> Part 2/2

(Main.java was attached)

## Solution

This is stupid and everything is stupid.

Let's start from the top and work down.

The first function is the same as we saw in the other rev (I am way to lazy to find the name, go figure it out yourself).

We do the same reversing operation (check parity then add/subtract).

The second function shifts the string by 3 and adds 2 to the charcode. Just shift it back and subtract.

The third function is literally base64 encoding, so we just decode.

The fourth function xors each character with 3. xor can be reversed by...xoring again, so we just xor everything with 3 again.

The last function just subtracts 1 from the charcode but repeats it an arbitrary amount of times (as determined by a stupid function).

You could honestly just skip the arbitrary thing and guess the flag, but the function is determined by the index (which doesn't change) so we can just reuse the function and skip characters to get past the repetition.

```
cctf{https://tinyurl.com/qtd2ref}
```