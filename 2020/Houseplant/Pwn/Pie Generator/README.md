# Houseplant CTF - Pie Generator

* **Category:** Pwn
* **Points:** 50

## Challenge

> This website lets you make a pie and have it too!
> 
> http://challs.houseplant.riceteacatpanda.wtf:30007
> 
> Dev: Jess

## Solution

Upon loading the page, we're prompted to guess a number. My first thought was that the challenge was similar to JS Lotto, but we don't really know what PRNG is being used, so it's kind of impossible to predict.

Inspecting source reveals a `setts()` function:
```
function setts() {
	document.getElementById("ts").value=(Date.now() / 1000000);
}
```

All the function does is set the value of the hidden `ts` input box to the current timestamp. Submitting the form calls this function. This looks suspiciously like a seed, so we just overwrite the function.

```
function setts() {
	document.getElementById("ts").value=5;
}
```

We guess a random value and submit.

![](./images/niceOne.jpg)

Reloading the page, we overwrite the `setts()` function again and guess `1`.

![](./images/imAGenius.jpg)


```
rtcp{w0w_sO_p53uD0}
```