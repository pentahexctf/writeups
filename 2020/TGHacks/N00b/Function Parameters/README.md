# TG:Hack 2020 – Function Parameters

* **Category:** n00b
* **Points:** 71

## Challenge

> Create a function that takes one parameter, a, and returns (a * 4) + 3. The C declaration would look like this:
```c
int func(int a)
{
    return (a * 4) + 3;
}
```
> `nc shellcode.tghack.no 1111`
> Note: This is level 5. End your assembly code with a line containing EOF.

## Solution

On x86-64 architecture, the function parameters, in order, are `rdi`, `rsi`, `rdx`, `rcx`, `r8`, and `r9`. This will come in more useful later, but for now we just need the first parameter.

Our assembly code is:
```
mov rax, rdi
mov rdi, 0x04
mul rdi
add rax, 0x03
ret
EOF
```

```
TG20{parameters_sure_are_nice_to_have}
```