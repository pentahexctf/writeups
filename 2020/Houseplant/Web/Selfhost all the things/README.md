# Houseplant CTF - Selfhost all the things!

* **Category:** Web
* **Points:** 1566

## Challenge

> The amount of data that online services like Discord and Instagram collect on us is staggering, so I thought I'd selfhost a chat app!
> 
> http://challs.houseplant.riceteacatpanda.wtf:30005
> 
> The chat database is wiped every hour.
> 
> This app is called Mantle and is open source. You can find its GitHub repo at https://github.com/nektro/mantle.
> 
> Dev: Tom
> 
> Hint! discord more like flag

## Solution

I...accidentally solved this challenge very quickly.

Upon loading the page, we're presented with a login page asking us to select our provider. The only option is `discord`. I remembered the hint, and thought it would be funny if I changed the value from `discord` to `flag`.

Turns out this was the solve.

I never even got to chat :c


```
rtcp{rtcp-*is-s/ort-of-se1fh0st3d}
```