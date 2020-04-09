# TG:Hack 2020 – Division

* **Category:** n00b
* **Points:** 67

## Challenge

> The `rax` register will be set up to contain a random value. Use the `div` instruction to divide `rax` by 4.
> `nc shellcode.tghack.no 1111`
> Note: This is level 3. End your assembly code with a line containing EOF.

## Solution

This is a textbook example of the `div` instruction.

Our assembly code is:
```
mov rdi, 0x04
div rdi
EOF
```

```
TG20{look_ma_im_a_math_wiz}
```