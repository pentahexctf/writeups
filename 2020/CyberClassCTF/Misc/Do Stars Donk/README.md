# CyberClassCTF - Do Stars Donk?

* **Category:** Misc
* **Points:** 250

## Challenge

> This is an osint challenge.
> 
> Hello there! I like to read and write things on Webtoon. PS. My favorite constellation is that of a fox PPS. My favorite number is 12. -Ghost
> 
> Part 1/2 for OSINT

## Solution

OSINT. My favorite thing.

Sarcasm does not translate well through text, so I will say it now: that was sarcastic.

The fox constellation is Vulpecula (thanks, Science Olympiad!). We search for the phrase "Vuplecula Webtoon" and find a Webtoon written by "kot & snoc".

The organizers are clearly acting in a very ethical manner and are using their challenges to advertise their webtoons.

Opening `Ep. 12 - Escape`, we skip the comic (although I have been told that one of the characters was somewhat vaguely kind of possibly inspired by me, so you should read the comic and give me an ego boost) and scroll to the bottom.

![](./images/b64garbage.jpg?raw=true)

Decoding this base64 string, we get the following phrase:

```who is snocbeef? Stalk them *ig* ?```

Instagram challenges are notoriously hard to do without an Instagram account, but I rally all of my immense technical ability and access the profile anyways.

![](./images/veryniceprofile.jpg?raw=true)

The account description/bio/whatever has a link: https://pastebin.com/4HzbhgkW

![](./images/pastebin.jpg?raw=true)

We take the link and bruteforce with rot (n=3) and find a Discord link: https://discord.com/channels/744782244941529130/744782245377867818/745048163466870836

These stupid things are impossible to access unless you click on them from inside of a discord message, so I send the link to the challenge creator to express my displeasure.

![](./images/revenge.jpg?raw=true)

The link leads us to a message in the CyberClass discord, which links to another Pastebin.

![Yay! I'm in the image!](./images/yetanotherpastebin.jpg?raw=true)

We finally end our search here.

![](./images/pastebinthethird.jpg?raw=true)


```
cctf{twink1e_t03s_f0x}
```