# Houseplant CTF – PZ

* **Category:** Reverse Engineering
* **Points:** 50 Points

## Challenge

> Ok, I think I made it slightly better. Now you won't get the flag this time!
> 
> Dev: William

(pass1.py was attached)

## Solution

The `main()` function is called at runtime. `main()` calls `checkpass()`, so the that's the correct flag.


```
rtcp{iT5_s1mPlY_1n_tH3_C0d3}
```