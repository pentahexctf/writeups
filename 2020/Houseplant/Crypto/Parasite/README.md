# Houseplant CTF - Parasite

* **Category:** Crypto
* **Points:** 784

## Challenge

> paraSite Killed me A liTtle inSide
> 
> Flag: English, case insensitive; turn all spaces into underscores
> 
> Dev: Claire
>
> Hint! Make sure you keep track of the spacing- it's there for a reason

(Parasite.txt was attached)

## Solution

Upon opening the attached, we find what appears to Morse, but decoding just yields gibberish.

``
JDU MEK KDF PUF PTK JEF LU GEUK CHK KUW FU BE
``

Looking back at the challenge description, we notice that the capitalized words spell out SKATS. A quick Google search reveals that this is a system to map Hangul characters to Latin letters.

I wrote a really, really, *really* bad script for this. We'll do a bit of data correction in a second.

After running the script, we get the following output.

```
ㅎㅡㅣ
ㅁㅏㅇ
ㅇㅡㄴ
ㅈㅣㄴ
ㅈㅓㅇ
ㅎㅏㄴ
ㄱㅣ
ㅅㅏㅣㅇ
ㅊㅜㅇ
ㅇㅣㅂ
ㄴㅣ
ㄷㅏ
```

There are two issues with this. First of all, `GEUK` should have been transliterated as `ㅅㅐㅇ`. This is because my code does not account for the TU, EU, SU, and IU transliterations. 

The second issue, obviously, is that the words aren't actually...words. My Korean friend read the above output and immediately identified and translated the characters. 

Unfortunately, "Korean friend" doesn't appear to be an easy-to-download package. As an alternative, we use a Korean keyboard to combine the characters in the output (Google translate, your phone, most things work).
```
희 망 은 진 정 한 기 생 충 입 니 다
```

This translates to "Hope is a true parasite," which gives us our flag


```
rtcp{hope_is_a_true_parasite}
```
```