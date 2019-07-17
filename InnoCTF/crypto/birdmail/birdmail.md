# InnoCTF - Bird Mail!

* **Category:** Crypto
* **Points:** 415

## Challenge

> We don't have chall text but something about RFC 1149

![](./cryptobirds.png?raw=true)


## Solution

After noticing the repetition of some birds, we concluded it was some substitution cipher. In order to solve, just go down the alphabet for every new bird.

![](./Untitled.png?raw=true)

Then simply plug it into a substitution decoder and brute force the flag

![](./unknown.png?raw=true)

```
InnoCTF{only_birds_everywhere}
```
