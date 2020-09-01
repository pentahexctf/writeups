# CyberClassCTF - Revvin' my Cj7

* **Category:** Rev
* **Points:** 150

## Challenge

> Snoc has inherited an old CJ7! Now she is [revvin' her CJ7](https://www.youtube.com/watch?v=D87hTPD9GEY). But there is a password. Find the flag.

(Main.java was attached)

## Solution

The encrypt() function basically splits the string in two, reverses the second half, and then recombines.

Some simple python code will undo that.


```
cctf{fL1pp17y_fL0pp1ty_b0nk}
```