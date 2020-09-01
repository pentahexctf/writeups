# CyberClassCTF - donkey-embly

* **Category:** Rev
* **Points:** 150

## Challenge

> What does donkeyembly(0xA) return? Submit the answer as a hexadecimal number in flag format, for example: cctf{0x30B}.
> 
> This is the beginning of a 3 part assembly series.

(donkeyembly.txt was attached)

## Solution

I'm too lazy to turn the assembly into pseudocode but basically the input is compared to the hex value 0x4. In our case, the input is greater, so 1 is added to the value and then it's returned.

**Note:** The organizers are bad and sad and garbage, so the flag was `cctf{0x9}`. This was wrong. The answer *should* be `cctf{0xB}`.

```
cctf{0x9}
```