# Houseplant CTF – JS Lotto

* **Category:** Misc.
* **Points:** 1973 Points

## Challenge

> I found this lotto website called JS Lotto. Wanna test your luck? I heard if you guess all 5 numbers correctly, you can win a flag!
> 
> http://challs.houseplant.riceteacatpanda.wtf:30006/
> Dev: jammy

## Solution

I liked the concept for this challenge, but unfortunately a script to solve this exact problem already existed online. I took first blood on this challenge though, which I was pretty happy about.

Opening the website we see a webpage that asks us to input five numbers from 0 to 1000.

![](./images/challenge.png)

Opening the source code of the we site, we see a `app.js` which sends and recieves requests from the server. In the code there are references to `Math.random()`, which makes me think that the backend server is also generating its numbers this way.

Doing some research into predicting `Math.random()`, we find [this](https://blog.securityevaluators.com/hacking-the-javascript-lottery-80cc437e3b7f) page, which talks about using a script to predict virual Powerball lottery numbers generated in JS. Hmmm...

They provide a link to a GitHub with a Python script that uses Z3 to solve for the state.

I edited the script to connect it to the `/guess` endpoint. First, the script requests for 5 numbers, turns them into `Math.random()` floats, then solves for the state using Z3. Then, the next 500 numbers are generated. A second request is sent to get 5 more numbers to figure out where in my predicted numbers the server currently is. Finally, the next 5 numbers after that point are the answer sent to the server, which gives the flag!

```
rtcp{th3_h0us3_d1dnt_w1n_th15_t1m3_5bcbf4}
```