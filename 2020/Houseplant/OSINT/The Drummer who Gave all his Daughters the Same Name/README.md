# Houseplant CTF – The Drummer who Gave all his Daughters the Same Name

* **Category:** OSINT
* **Points:** 50 Points

## Challenge

> What is the value stored in the first registry key created by the virus Anna Kournikova?
> 
> Hint! No flag format :)

## Solution

Google reveals that HKCU\software\OnTheFly\mailed is set to `1`, but this isn't accepted.

I read through the [source](https://packetstormsecurity.com/files/24379/AnnaKournikova-source.txt.html) and notice that earlier in the code, HKCU\software\OnTheFly\ is set to `Worm made with Vbswg 1.50b`. This [paper](https://www.cse.msu.edu/~enbody/virus/Final_TermPaper_AnnaKournikova_Avi.pdf) and this [paper](https://www.giac.org/paper/gsec/644/malicious-code-vbs-onthefly-anna-kournikova/101208) both verify this answer.


```
Worm made with Vbswg 1.50b
```