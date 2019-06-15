# flagCTF – No Comment

* **Category:** Web Exploitation
* **Points:** 10

## Challenge

> Visit http://18.217.184.75:8002/
> You don't see the flag, huh? Don't get lost browsing to other pages yet, try looking like a computer does.

## Solution

Judging from the title, the flag is probably stored as a comment. We view source, and sure enough, there's a comment with the flag on the webpage.

```
Th3r3I$M0reToTh1sThanMeetsTh3Eye
```