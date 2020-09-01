### Difficult Decryption
Just use sympy lol.

```python
from sympy.ntheory.residue_ntheory import discrete_log
g = 5
r = 232042342203461569340683568996607232345
n = 491988559103692092263984889813697016406

your_key = 76405255723702450233149901853450417505
enc = 12259991521844666821961395299843462461536060465691388049371797540470
a = discrete_log(n,r,g)
print(bytes.fromhex(hex(enc ^ (pow(your_key, a, n)))[2:]))
# b'tjctf{Ali3ns_1iv3_am0ng_us!}'
```

```
tjctf{Ali3ns_1iv3_am0ng_us!}
```

**Note from Drakon:** Yeah, there's no explanation for this challenge, and I really don't want to write one either. Basically, it was Diffie-Hellman with a nonprime modulus.