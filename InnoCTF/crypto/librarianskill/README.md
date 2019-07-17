# InnoCTF - Librarian Skill

* **Category:** Crypto
* **Points:** 484

## Challenge

> Read between lines!
ls.zip containing 1984.txt, Animal Farm.txt, The Catcher in the Rye.txt, and the cipher

![](./ls/cipher.jpg)


## Solution

At first, we followed the rules of a simple book cipher and gathered the n-th word from all texts to see if we could manipulate them to make a string or sentence. That didn't work. Later, someone pointed out that the picture of the cipher might have been referencing the Beale cipher which was created by a pirate which what the picture was of. By pasting the contents of each text individually with a single row of the cipher into a Beale Cipher decoder, we broke it down to "hurry", "slowly", "netboss" which was the arrangement of the first letter of the n-th word. By putting the flag in as InnoCTF{hurry_slowly_quickly} didn't work. Later we realized we needed to maintain the capitalization of each character from the text itself.

''' <-replace with `
InnoCTF{Hurry_slowly_NETboss}
''' <-replace with `
