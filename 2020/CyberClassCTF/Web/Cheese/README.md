# CyberClassCTF - Cheese

* **Category:** Web
* **Points:** 150

## Challenge

> You have been tasked with a delivery. (http://challenges.ctfd.io:30045/cheese/)

## Solution

Don't even bother looking at the site. Look at source.

The login page links to `notsuccess.html`. Some ~~guessctf~~ deductive reasoning skills lead us to the flag, located at `success.html`.


```
cctf{did_y0u_use_dynam1te}
```