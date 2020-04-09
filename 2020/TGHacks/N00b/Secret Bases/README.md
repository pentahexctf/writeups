# TG:Hack 2020 – Secret Bases

* **Category:** n00b
* **Points:** 58

## Challenge

> We managed to extract this secret information from one of Mother's 64 secret bases before we had to leave Earth. Are you able to decode it?
> ``VEcyMHt5b3VfY2FuX25ldmVyX2hhdmVfZW5vdWdoX3NlY3JldF9iYXNlc30=``

## Solution

The data is obviously base64, judging from the challenge description and the padding at the end. We decode for the flag.

```
TG20{you_can_never_have_enough_secret_bases}
```