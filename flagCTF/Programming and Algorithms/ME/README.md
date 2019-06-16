# flagCTF - ME!

* **Category:** Programming and Algorithms
* **Points:** 45

## Challenge

> "You can't spell 'awesome' without 'me'!" -- Taylor Swift/Brendon Urie, "ME!" (2019)
>
> Even with all that you hear in pop songs these days, that is a true statement! You wonder how many words are spelled with the letters 'm' and 'e' in that order, but not necessarily consecutive.
> 
> You are given a list of words, and must determine how many satisfy this property.
> 
> Input format:
> 
> The first line contains the integer N (1 <= N <= 1000), the number of lines to follow. Each of the subsequent N lines contains one of the words in question. The length of each word is at most 500,000 characters. They are not guaranteed to be English words, or words in any language.
> 
> Output format: One line, containing the number of words that satisfy that property.
> 
> Example input:
> 
> 5
> 
> awesome
> 
> lime
> 
> mine
> 
> eminem
> 
> emotion
> 
> Example output:
> 
> 4
> 
> Output description:
> 
> The first 4 of the 5 words given satisfy that property. The words 'awesome' and 'me' are clear. In 'mine', the letters are not consecutive, and in 'eminem', we can use the first 'm' and the second 'e'. However, the only 'e' in the fifth word, 'emotion' is before the 'm', so this does not count.
> 
> Flag format:
> 
> Submit the answers for all 5 input files in order, delimited by semicolons. For example, "4;902;489;103;670".

## Solution

All we have to do is iterate through the letters in each word. If we encounter the letter "m", we trigger a flag. If, after that, we encounter the letter "e", then we break and increment a counter by one. Otherwise, we move on to the next word.

```
4;957;245;0;440
```