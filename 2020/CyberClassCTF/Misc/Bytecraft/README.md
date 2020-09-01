# CyberClassCTF - Bytecraft

* **Category:** Misc
* **Points:** 400

## Challenge

> Barn has made a huge redstone contraption! What is its message once all the lights turn on? The message is encoded in the redstone signal.
> 
> All of the chests are empty and they can be filled with stackable items. An example module of the contraption is given for you to examine.
> 
> Flag format is the regular flag format.
> 
> [Minecraft redstone](https://minecraft.gamepedia.com/Mechanics/Redstone/Circuit#Power)

(example.png and hugeRedstoneContraption.png were attached)


## Solution

The question description was frankly badly written and difficult to interpret. I decided to give up on this challenge and come back to it once clarification arrived.

Clarification did not arrive.

I contacted the challenge author and ~~interrogated~~ kindly asked him to explain exactly how the challenge worked.

Apparently, you were supposed to determine the required signal amount to activate each redstone lamp.

Since the signals went into the double digits, I assumed they were encoded as hex. This yields `63 63 74 66 7b 33 70 31 63 5f 6d 31 6e 33 63 72 34 66 74 32 39 34 65 7d`. Note that it is `70` and not `71`, since the lamp in that segment was already on.

```
cctf{3p1c_m1n3cr4ft294e}
```