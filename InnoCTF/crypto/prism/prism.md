# InnoCTF - Prism

* **Category:** Misc
* **Points:** 223

## Challenge

> Do you have a prism to take a closer look?

![](writeups/InnoCTF/misc/prism/images/qrcode.png)

## Solution

At first look, since it's a photo we looked through metadata and steganography but came up with nothing. The name of the challenge got me thinking about separating the red, green, and blue. Another thing I took note of was a odd string when scanning the QR code. Thus, I separated the three colors using photoshop and got three different QR codes. The flag is retrieved by concatenating the three outputs.
Red only:
![](writeups/InnoCTF/misc/prism/images/redonly.png)
InnoCTF{gZmLFg

Green only:
![](writeups/InnoCTF/misc/prism/images/greenonly.png)
pflkF5hbwBlA0h

Blue only:
![](writeups/InnoCTF/misc/prism/images/blueonly.png)
myPUkPPcugKhY}

```
InnoCTF{gZmLFgpflkF5hbwBlA0hmyPUkPPcugKhY}
```
