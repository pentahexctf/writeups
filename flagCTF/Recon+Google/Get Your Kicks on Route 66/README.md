## Get Your Kicks on Route 66

```
# flagCTF – Get Your Kicks on Route 66

* **Category:** Reconnaissance, Google, and Open Source Intelligence
* **Points:** 20

## Challenge

> UPDATE: Added "in the US" -- this was erroneously missing from the first statement.
> As of the start of 2019, how many incorporated cities or towns in the US have the
> substring "flag" (case insensitive) in them, and what is the first one alphabetically?
> The flag is these two answers separated by a semicolon. For example, if there are 31 
> such cities and the first one alphabetically is "Six Flags", submit "31;Six Flags" 
> without the quotation marks.

## Solution

I searched for "list of incorporated cities and towns in the us type:text" on Google. By specifying type, the site simplemaps.com came up and I downloaded the CSV. By filtering for flag and True in the incorporated column (also the only boolean), I got 7 unique lines.

grep -i flag uscitiesv1.5.csv | grep True

"Marineland","Marineland","FL","Florida","12035","Flagler","29.6648","-81.2138","17","17","24","polygon","True","America/New_York","32137","1840017221"
"Bunnell","Bunnell","FL","Florida","12035","Flagler","29.4198","-81.3235","2907","2907","8","polygon","True","America/New_York","32110","1840014036"
"Palm Coast","Palm Coast","FL","Florida","12035","Flagler","29.5389","-81.2460","401757.0","86516","351","polygon","True","America/New_York","32164 32136 32137 32135 32142","1840015064"
"Beverly Beach","Beverly Beach","FL","Florida","12035","Flagler","29.5164","-81.1475","400","400","453","polygon","True","America/New_York","32136","1840015947"
"Flagler Beach","Flagler Beach","FL","Florida","12035","Flagler","29.4711","-81.1300","5068","5068","534","polygon","True","America/New_York","32136 32143","1840014035"
"Flagler","Flagler","CO","Colorado","08063","Kit Carson","39.2955","-103.0767","549","549","166","polygon","True","America/Denver","80815","1840021447"
"Flagstaff","Flagstaff","AZ","Arizona","04005","Coconino","35.1872","-111.6195","78628.0","71975","421","polygon","True","America/Phoenix","86001 86011 86004 86002 86005","1840020335"

Only the last 3 have flag in the actual city name, so the answer is "3;Flagler Beach"

```
3;Flagler Beach
```
```
