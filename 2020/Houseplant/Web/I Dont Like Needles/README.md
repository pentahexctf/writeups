# Houseplant CTF - I don't like needles

* **Category:** Web
* **Points:** 50

## Challenge

> They make me SQueaL!
> 
> http://challs.houseplant.riceteacatpanda.wtf:30001
> 
> Dev: Tom

## Solution

A quick glance through the source yields a comment: `<!-- ?sauce -->`

Appending this to the URL gets us the full source of the document, which makes life really easy. A quick glance through the source reveals the the flag is only returned if the user is `flagman69`. So, a simple SQL injection won't work.

Since we can see the exact SQL statement, writing an injection is extremely easy. Sure, you could write a fancy UNION injection, but I'm lazy.

We can inject `lmaomeme` in for the user and `' or username='flagman69' and 'a'='a` for the password. This makes the statement effectively ``SELECT * FROM users WHERE username='lmaomeme' AND password='' or username='flagman69' and 'a'='a'``. This will only select one user - the `flagman69` user.

**Note:** If you're *not* lazy like me and you want to write an actually good statement, you can do the following UNION injection: `' AND 1=2 UNION SELECT * FROM users WHERE username ='flagman69' AND '1'='1`.


```
rtcp{y0u-kn0w-1-didn't-mean-it-like-th@t}
```