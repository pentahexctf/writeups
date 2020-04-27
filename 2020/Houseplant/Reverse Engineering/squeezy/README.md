# Houseplant CTF – EZ

* **Category:** Reverse Engineering
* **Points:** 50 Points

## Challenge

> Ok this time, you aren't getting anywhere near anything.
> 
> Dev: William

(pass3.py was attached)

## Solution

`main()` is called at runtime. `main()` in turn calls `checkpass()`. `checkpass()` takes user input, then calls `whoah(key,userinput)`. It then base64 encodes the valued returned, comparing it to `HxEMBxUAURg6I0QILT4UVRolMQFRHzokRBcmAygNXhkqWBw=`.

A quick inspection indicates that `whoah(s1,s2)` is a simple XOR implementation. Since we have the key and the base64 encoded ciphertext, we can easily reverse the plaintext.

A Python implementation is possible, but I just used CyberChef.


```
rtcp{y0u_L3fT_y0uR_x0r_K3y_bEh1nD!}
```