# CyberClassCTF - Do Stars Donk? - Pt. 2

* **Category:** Misc
* **Points:** 300

## Challenge

> Continuation of Do Stars Donk.

## Solution

More OSINT.

Let's continue from the previous challenge.

![](./images/pastebin.jpg?raw=true)

I'm actually not sure what cipher was used on this link, but it's clearly a monoalphabetic substitution cipher, so we can just manually solve it.

In the end, we have the following letter relationship, which yields https://www.wattpad.com/story/237288985-do-stars-donk

![](./images/totallynotabash.jpg?raw=true)

I'm not in the mood to suffer, so I skip the entire story. In the comments, we find a username.

![](./images/comment.jpg?raw=true)

This looks suspiciously like the famous ~~CollegeBoard spy~~ fellow student dinosauce11, so we decide to check Reddit.

The Reddit account has 2 posts, one of which is named "Flag". Checking the post, we find a single comment from another user: frogthightempura

The organizers hid the flag in the porilfe description, forcing us to go away from the glorious Old Reddit into the horrifying ugly sin that is "New Reddit".

![](./images/SIN.jpg?raw=true)


```
cctf{1ve_d3cided_th4t_stars_DO_d0nk}
```