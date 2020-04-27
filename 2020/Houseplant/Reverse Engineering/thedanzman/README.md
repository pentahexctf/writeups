# Houseplant CTF – thedanzman

* **Category:** Reverse Engineering
* **Points:** 50 Points

## Challenge

> Fine. I made it even harder. It is now no longer "ez", "pz", "lemon" or "squeezy".
> You will never get the flag this time.
> 
> Dev: William
> 
> Hint! This should be no problem if you look at the previous ones.

(pass4.py was attached)

## Solution

`main()` is called at runtime. `main()` in turn calls `checkpass()`. `checkpass()` takes user input, and calls `nope(key,userinput)`. It base64 encodes the result, runs rot13 on the base64 encoded text, then calls `wow(d)`.

A quick inspection indicates that `nope(s1,s2)` is a simple XOR implementation, and `wow(x)` just reverses it's input.

So, we take `'=ZkXipjPiLIXRpIYTpQHpjSQkxIIFbQCK1FR3DuJZxtPAtkR'o`, reverse it, then run ROT13. This is byte string, so we remove the leading `b'` and the trailing quote.

We can base64 decode the above string, then XOR it. The key can be obtained by running ROT13 on `nyameowpurrpurrnyanyapurrpurrnyanya`.


```
rtcp{n0w_tH4T_w45_m0r3_cH4lL3NgiNG}
```