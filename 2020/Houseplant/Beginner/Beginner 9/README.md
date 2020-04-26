# Houseplant CTF - Beginner 9

* **Category:** Beginner
* **Points:** 50

## Challenge

> Hope you've been paying attention! :D
> 
> Remember to wrap the flag with rtcp{}
> Hint! we stan cyberchef in this household

(Beginner 10.txt was attached)
## Solution

This isn't even my final form!

Anyways, I'm going to do an actual writeup for this challenge because apparently some teams actually had trouble with this.

The first layer is fairly straightforward. We can pretty easily identify it as base64. 

This decodes to what appears to be hex encoded data (for the sake of brevity, I won't paste that text here nor will I include it as a file - you should be able to get it yourself pretty easily).

The hex data decodes to a bunch of dots and dashes. Decoding from Morse, we get what look like binary characters.

Well, it could be Baconian, but a quick test easily verifies that it is not. From there, we get what appears to be an A1Z26 cipher.

This last step was actually *kind of* hard, because we don't have any known plaintext. There are probably some fancy tools you can do to get a good idea of the plaintext (some sort of analysis tool comes to mind). However, since the chall description heavily suggests that this challenge is based off of the previous challenges, we can safely assume that the only cipher in use are ones that have already been used.

The only ciphers that we've seen that could apply to this text are atbash, rot13, and *maybe* base64.

A quick test of the possible combinations quickly reveals that the last two steps are atbash and rot13.

**As a quick note:** CyberChef is love, CyberChef is life. The magic function would have effortlessly decoded the text down to the atbash step.


```
rtcp{nineornone}
```