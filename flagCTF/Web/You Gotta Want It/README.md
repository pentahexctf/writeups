# flagCTF – You Gotta Want It

* **Category:** Web Exploitation
* **Points:** 30

## Challenge

>http://18.217.184.75:8002/wantflag.html
>
>For help with this challenge, tune into the stream at 6:50 pm ET
>
>Scope of attack: http://18.217.184.75:8002/

## Solution

Upon loading the page, we're presented with two options: "No" and "Definitely No". Both options just return "Alright, I won't give you the flag. If you insist."
When we view the source for the page, we find that both of the options have an assigned value of 0. Inspect element, and replace one of the values with 1.


```
1502af955e0a8f5ac6a5529550660c33
```