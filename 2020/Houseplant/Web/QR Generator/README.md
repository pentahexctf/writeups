# Houseplant CTF - QR Generator

* **Category:** Web
* **Points:** 50

## Challenge

> I was playing around with some stuff on my computer and found out that you can generate QR codes! I tried to make an online QR code generator, but it seems that's not working like it should be. Would you mind taking a look?
> 
> http://challs.houseplant.riceteacatpanda.wtf:30004
> 
> Dev: jammy
> 
> Hint! For some reason, my website isn't too fond of backticks...
## Solution

The webpage appears to generate QR codes from a user-supplied input. Checking the source tells us nothing, except that the QR code apparently only takes the first character of input.

The hint is the important part - we find that backticks are apparently an issue. Sure enough, providing a single backtick as input gives us an error. We deduce that the challenge is mostly likely command injection.

To test this, we input `\` cat /etc/passwd \``. Decoding gives us the character "r", which is (almost always) the first character of the /etc/passwd file.

From here, the challenge is easy. We can use a variety of methods to iterate through the characters in `flag.txt`. I considered using a combination of `head` and `tail` and `sed`, but finally settled on `dd`. My teammate used a combination of `tr` and `cut`.

I've uploaded my script (which I wrote while creating this writeup) as `drakon_solve.py` and I've uploaded the script that we used during the competition as `strellic_solve.py`.
Frankly, the implementation isn't that important.


```
rtcp{fl4gz_1n_qr_c0d3s???_b1c3fea}
```