# TG:Hack 2020 – Mega Shifting

* **Category:** n00b
* **Points:** 65

## Challenge

> Many of our scientists shifted this message around. Now the AI can't solve it with frequency analysis. However, we know that the key length is 3.
> ``Js tes ynzevbz osavbw. Js znjx gvx NW ihfibgx. Jwmu bh tcty wm jol wilg sqvgmvbz.
Ysm hg abdx vh wbsl acm swgq havg drm. MT20{havg_fhgm_fhtl_vbqrxa}``

## Solution

We challenge name and the description hint that this is some sort of keyed shift. This, coupled with the comment on "frequency analysis" indicates that the cipher being used is most likely vigenere.

Vigenere has been broken and can be cracked with frequency analysis methods. This process is made easier with longer ciphertexts or knowledge about the key.

We use an online tool (really, any will do) and supply the key length (3). 

The key is "NOT" and the plaintext is:
```We are falling behind. We gave the AI purpose. With no goal it was just existing.
Let us hope it does not find this key. TG20{this_must_stay_hidden}```

```
TG20{this_must_stay_hidden}
```