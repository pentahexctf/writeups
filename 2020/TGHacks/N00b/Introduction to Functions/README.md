# TG:Hack 2020 – Introduction to Functions

* **Category:** n00b
* **Points:** 69

## Challenge

> Create a function that takes no parameters and returns 0. You only have to write the function body.
> `nc shellcode.tghack.no 1111`
> Note: This is level 4. End your assembly code with a line containing EOF.

## Solution

On x86-64 architecture, the return value is in `rax`.

Our assembly code is:
```
mov rax, 0x00
ret
EOF
```

```
TG20{is_this_functional_programming?}
```