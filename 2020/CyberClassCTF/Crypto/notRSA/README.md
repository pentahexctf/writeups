# CyberClassCTF - notRSA

* **Category:** Crypto
* **Points:** 500

## Challenge

> Ok we've learned our lesson. We've made our modulus really big this time and even doubled our exponent! It's so secure that even we're having trouble decrypting it.

(notRSA.txt was attached)

## Solution

I spent a bunch of time trying to attack this before I noticed that n was prime. That...does a lot.

Also, e is doubled - this is important, because this makes it not coprime with the modulus.

So, we can do some rabin magic.

*jason please explain*

Just refer to the official writeup to be honest. I bumbled my way through this.

```
cctf{rabin_but_with_extra_steps}
```