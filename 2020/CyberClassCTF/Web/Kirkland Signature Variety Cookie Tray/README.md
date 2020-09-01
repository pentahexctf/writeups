# CyberClassCTF - Cheese

* **Category:** Web
* **Points:** 200

## Challenge

> You are trying to buy cookies from Costco, but you keep trying to break into the cookie storage room, where you are not allowed! (:thonk:) Find the flag. http://challenges.ctfd.io:30045/cookies/

## Solution

We're presented with a login page. Our first instinct is to perform a sql inject. While this doesn't give us access, we still manage to log in.

Examining cookies, we immediately see an `admin` cookie. Changing to to `True` yields the flag.


```
cctf{ask_nic3ly_4nd_you11_g3t_c00k13s}
```