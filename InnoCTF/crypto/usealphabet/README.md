# InnoCTF - Use Alphabet!

* **Category:** Crypto
* **Points:** 763

## Challenge

> We don't have chall text but it was something about "The German Friend"

![](./images/task.png)

## Solution

At first look, it seems like a standard ADFGVX cipher. The problem was that we didn't know the key. Someone pointed out that the name might by pointing to the 26 characters + 0 - 9. By plugging that as the key we get this string:

![](./images/dcode.png)

At first, this scrambled string looks useless; however, a closer inspection led us to realize "BERLIN"  and "1941", both seemingly related to the chall text. By reading up on the implications of the ADFGVX cipher we noticed that the structure of the table in the task was not in order but rather organized alphabetically as dictated by the cipher. By substituting the cipher with the string we have and rearranging it by the key word "BERLIN", we receive our flag.

![](./images/rearrange.png)

```
InnoCTF{drang_nach_osten_1941}
```
