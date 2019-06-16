# flagCTF – Can't Get It Out Of My Head

* **Category:** Reconnaissance, Google, and Open Source Intelligence
* **Points:** 50

## Challenge

> The lyrics in pop music might seem to be getting more repetitive and predictable these days (and in fact, they are: https://pudding.cool/2017/05/song-repetition/). What about the titles?
> 
> How many Billboard Hot 100 hit tracks from 1960-2009 are the exact same title as the name of the credited artists, including any collaborators, and what is the first one alphabetically? For example, if the song by "The The" called "The The" had charted in 1981, that would count as 1, but if they instead charted songs titled "The" or "The The The", those would not count. If there were also exactly 2 other such songs later in the alphabet, you would submit "3;The The"

## Solution

I searched for a database of the Billboard Hot 100 hit tracks, and find a CSV file here: https://data.world/kcmillersean/billboard-hot-100-1958-2017

You need an account to download files, but registration is free so I went ahead and just grabbed it. We use a quick python script to grab the list of songs that match our criteria, sort, and grab length.

```
6;Chairman of the Board
```