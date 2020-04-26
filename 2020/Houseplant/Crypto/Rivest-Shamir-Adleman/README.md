# Houseplant CTF - Rivest Shamir Adleman

* **Category:** Crypto.
* **Points:** 338

## Challenge

>A while back I wrote a Python implementation of RSA, but Python's really slow at maths. Especially generating primes.
>
>Dev: Tem

## Solution

Opening the zip file provided, we see that there is a script for decrypting, encrypting, and for generating keys for RSA, which is from the title of the challenge. There's also a pre-generated public key, which we can assume was used for encrypting the received ciphertext in the zip, and a file called "component.txt", which contains a large number. Looking at the public key file, we can see that N is pretty long, at 616 digits, and e is very small, at 5, suggesting that this might be weak RSA by low exponent.

But there's a different way to take on this problem, and it involves the component file. Checking the length of the number reveals that it is 308 digits, half of N's length. This means that it could be one of the primes factors of N, since RSA generally wants the primes to be around the same number of digits to make bruteforcing one of the factors(and thus the other by dividing N) more difficult. We check if N is divisible by component, and we see that it is! With this, we can factor N into p and q, obtain phi(N), and use mod inverse to get d from e and phi(N). Then, looking at the file format for ```private-key.json``` from the key generating script, we put the private key into a file and run decrypt.py on the encoded message.

The resulting flag is ```rtcp{f1xed_pr*me-0r_low_e?}```