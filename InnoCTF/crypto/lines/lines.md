# CTF NAME – CHALLENGE NAME

* **Category:** Crypto
* **Points:** 422

## Challenge

> We don't have chall text
![](InnoCTF\crypto\lines\lines.png)
## Solution

We find a picture with nodes affiliated with letters, numbers, and an underscore. Connecting the nodes are lines that eventually stop at two nodes. Manually tracing the lines both ways, we find:

```
1T_W4S_GO0DTAC71K5MEQN8
```
However the flag was required in lower-case for some random reason:
```
InnoCTF{1t_w4s_go0dtac71k5meqn8}
```
