# TG:Hack 2020 – Registers Everywhere

* **Category:** n00b
* **Points:** 65

## Challenge

> Set up the registers as follows:

Register name | Value
------------- | -----
rax	| 42
rbx	| 13
rcx	| 37
rdi	| 0
rsi	| 1337
> Good luck!
> `nc shellcode.tghack.no 1111`
> Note: This is level 2. End your assembly code with a line containing EOF.

## Solution

Some more basic assembly. Again, all we need is a `mov` statement.

Our assembly code is:
```
mov rax, 42
mov rbx, 13
mov rcx, 37
mov rdi, 0
mov rsi, 1337
EOF
```

```
TG20{some_setup_required}
```