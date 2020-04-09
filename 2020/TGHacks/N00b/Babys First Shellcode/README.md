# TG:Hack 2020 – Baby's First Shellcode

* **Category:** n00b
* **Points:** 75

## Challenge

> Time to write your first shellcode! Write shellcode that issues the syscall `exit` with a status code of `42`. The C equivalent would be something like: `exit(42)`.
> Good luck!
> `nc shellcode.tghack.no 1111`
> Note: This is level 7. End your assembly code with a line containing EOF.

## Solution

The syscall number for exit on x86-64 architecture should be 0x3c. The exit syscall only supports one parameter - the status code.

Our assembly code is:
```
mov rax, 0x3c
mov rdi, 0x2a
syscall
EOF
```

```
TG20{good_bye_noob_hello_shellcode}
```