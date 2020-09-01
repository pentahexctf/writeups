# CyberClassCTF - ponkey

* **Category:** Rev
* **Points:** 175

## Challenge

> Ponkey has written a Java program to check passwords! The program encrypts the password then checks it. What's the password?

(Main.java was attached)

## Solution

The encrypt() function goes through each character, then just outputs the character that comes 1, 2, 3, and 4 before it on the ASCII character chart. The simplest method is to take every 4 characters, then just take the character that come 1 after.

This is hard to say in English.

Basically, take the charcode and then add 1.


```
cctf{ponk3yM4N}
```