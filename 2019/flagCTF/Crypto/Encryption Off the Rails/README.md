# flagCTF – Encryption Off the Rails

* **Category:** Crypto
* **Points:** 15

## Challenge

> icetn fekit hanemasoraougseetaae 0al ipr hitnaiinraecpx;etpe nitr asmyost e li ftrnuesvnh pirm rg.:U1S.Trfep mseaei ccn m he chirtdaeaar, pi rvtpnt aaaamae teyoaeser gtn1sh echrue lx se at teetsnectx lx ng tb beeoh txanllg g i nrnptr aFaTscienetptpmohri eptaielcee -eefc ell3V

## Solution

The title hints that this ciphertext was encrypted with railfence. We bruteforce the number of rows and offset, and get pretty close with 5 rails and offset 3. It's not perfect, but we end up with:

```
he .ailTencr cifhereperpute  thm plsintext an aespeiifi  macnercto nake themcip erthxt;esin e tce chpheitexr ant pldintaxt ere anagaamsr it,may be possible to recover the plaintext of a natural-language message even if the encryption parameters are large. Flag: UtT3sn10S1cVis
```

Since the end is uncorrupted, I just hoped for the best and submitted the flag. It worked, so no complaints.

```
UtT3sn10S1cVis
```