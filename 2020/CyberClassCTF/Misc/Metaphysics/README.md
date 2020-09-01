# CyberClassCTF - Metaphysics

* **Category:** Misc
* **Points:** 100

## Challenge

> Metaphysics is a shadow cast on the wall of a cave. Can you find the flag?

(metaphysics.jpg was attached)


## Solution

You were probably supposed to use exiftool to get the metadata or something.

It doesn't matter, because JPEG metadata is stored in the header. Use a hex editor yet again.

```
cctf{have_you_escaped_the_cave}
```