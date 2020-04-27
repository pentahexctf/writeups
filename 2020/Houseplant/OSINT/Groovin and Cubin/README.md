# Houseplant CTF – Groovin and Cubin

* **Category:** OSINT
* **Points:** 50 Points

## Challenge

> I really like my work, I get to make cool cryptography CTF challenges but with Rubik's cubes! Sadly, they aren't good enough to get released, but hey, I took a nice image of my work! You should go try to find some more about my work :)
> 
> Dev: William
> Hint! Once you have a business name, try find some things on social media!
> Hint! BioTek is not the business name, but thank you for paying attention to my mousepad :) - william
> Hint! Any flags that are a lyric from https://www.youtube.com/watch?v=dQw4w9WgXcQ are not the correct flag, try looking harder on the page you were on to a link to another social media.

(vibin.zip was attached)

## Solution

Upon extracting, we're presented with vibin.jpg. Running `exiftool` yields us an interesting result:

```
Comment                         : A long day of doing cube crypto at work... but working at Groobi Doobie Shoobie Corp is super fun!
```

Googling "Groobi Doobie Shoobie Corp" gives us a Twitter account. We find a bunch of tweets (including a retweet of Elon-chan, nice). The oldest tweet on the account says:

```
Woah, now this is kinda cool! I really like not having to use that wacky Instagram site anymore. (Feel free to follow me @groovyshoobie tho)
It's kinda cool here! I think I'll stay here. 
Gotta go water the houseplants now though :)
```

Navigating to groovyshoobie on Instagram, we find the flag in the profile (bio? i don't use social media what is this called)


```
rtcp{eXiF_c0Mm3nT5_4r3nT_n3cEss4rY}
```