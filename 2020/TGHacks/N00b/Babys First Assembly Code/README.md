# TG:Hack 2020 – Baby's First Assembly Code

* **Category:** n00b
* **Points:** 64

## Challenge

> Zero out the `rax` register. Which means you have to set `rax` to 0. That's it!

> `nc shellcode.tghack.no 1111`
> Note: This is level 1. End your assembly code with a line containing EOF.

## Solution

This is super basic assembly. All we need is a `mov` statement.

Our assembly code is:
```
mov rax, 0
EOF
```

```
TG20{welcome_to_the_world_of_assembly}
```