# CyberClassCTF - Transcontinental Railway

* **Category:** Crypto
* **Points:** 200

## Challenge

> I'm trying to build a railroad here and I found this message on the golden spike. Can you help me find the flag?
> 
> CETOHCWLEOGLS}T{CMTEDUFOHR

## Solution

This is pretty obviously railfence. Since we know flag format, bruteforcing is trivial.

No offset, four rails.

```
CCTF{WELCOMETOTHEGOLDRUSH}
```