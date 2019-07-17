# InnoCTF - Bird Mail!

* **Category:** Crypto
* **Points:** 415

## Challenge

> We don't have chall text but something about RFC 1149

![](writeups/InnoCTF/crypto/birdmail/cryptobirds.png)


## Solution

After noticing the repetition of some birds, we concluded it was some substitution cipher. In order to solve, just go down the alphabet for every new bird.
![](writeups/InnoCTF/crypto/birdmail/Untitled.png)
Then simply plug it into a substitution decoder and brute force the flag
![](writeups/InnoCTF/crypto/birdmail/unknown.png)

```
InnoCTF{only_birds_everywhere}
```
