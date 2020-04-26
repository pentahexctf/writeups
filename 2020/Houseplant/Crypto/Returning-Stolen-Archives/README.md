# Houseplant CTF - Returning Stolen Archives

* **Category:** Crypto
* **Points:** 50

## Challenge

> So I was trying to return the stolen archives securely, but it seems that I had to return them one at a time, and now it seems the thieves stole them back! Can you help recover them once and for all? It seems they had to steal them one at a time...
> 
> Dev: William
> 
> Hint! Well you sure as hell ain't going to solve this one through factorization.

(intercepted.txt and returningstolenarchives.py were attached)



## Solution

One of the first things you'll notice when you open the intercepted text file is that there's a lot of ciphertexts. You can infer that each one is probably the result of encrypting a single character of the whole message, rather than one ciphertext containing the entire encrypted message. 

Knowing this, we can bruteforce the plaintext character for each ciphertext, since there aren't many printable characters. For each ciphertext, we can test the result of performing RSA encryption, which is implied from the challenge title and the given N and e from the intercepted file, on all the printable characters and check when the result matches the ciphertext. Then, concatenating the resulting plaintexts together should give us the flag.

```
rtcp{cH4r_bY_Ch@R!}
```