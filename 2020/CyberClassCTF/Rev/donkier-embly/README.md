# CyberClassCTF - donkier-embly

* **Category:** Rev
* **Points:** 300

## Challenge

> What does donkierembly(0x2B) return? Submit the answer as a hexadecimal number in flag format, for example: cctf{0x30B}.

(Main.java was attached)

## Solution

Once again, I'm too lazy to write the full pseudocode.

The input has 0x19 subtracted from it.

Then a for loop is run:

```c
for (i = 0; i <= 4; i++) {
	in ^= i
}
```

If the output of the above loop is greater than 0x16, it is returned. Otherwise, it is squared.

Since the output of the above loop is exactly 0x16, it is squared.

```
cctf{0x1E4}
```