# CyberClassCTF - Jason in a Bin

* **Category:** Misc
* **Points:** 250

## Challenge

> It's a beautiful summer day. You go to the park and see a snowman walking inside a trash bin, so you decide to take a picture. Find the flag.

(jasoninabin.png was attached)


## Solution

The solution is obviously to use `Binwalk`, but I'm too lazy to do that.

I looked through the file with a hex editor just in case the problem was stego (again) and ended up finding the ELF header by accident. It probably would have been easier with `binwalk`, but my paranoia towards stego challenges worked too.


```
cctf{binwalk_more_like_win_walk}
```