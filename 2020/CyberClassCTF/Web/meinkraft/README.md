# CyberClassCTF - meinkraft

* **Category:** Web
* **Points:** 250

## Challenge

> Get ~~punted~~ donked . http://challenges.ctfd.io:30045/meinkraft/

## Solution

This challenge was released last minute and was basically a tiebreaker between our team and the second place team. Understandably, we were somewhat stressed while we bashed our heads against it.

First thought is to try to register a user as admin/admin. We get an interesting error.

![](./images/error.jpg?raw=true)

Any CTF player worth their salt should instantly recognize this as rot13. Trying to register a user as admin/nqzva confirms our suspicions.

![](./images/10outof10security.jpg?raw=true)

We then spend the next minute trying progressively more and more complicated payloads while hoping that the other team hasn't solve it yet. Suddenly, we notice something on top.

![](./images/stupid.jpg?raw=true)

That's right. There's a login page.

5 seconds later and we have the flag.


```
cctf{untrustworthy_poptarts}
```