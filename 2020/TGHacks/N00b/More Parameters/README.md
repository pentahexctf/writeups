# TG:Hack 2020 – More Parameters

* **Category:** n00b
* **Points:** 72

## Challenge

> Create a function that takes two parameters, multiplies them together and returns the result.
> The equivalent in C would be something like this:
```c
int func(int a, int b)
{
    return a * b;
}
```
> Connect to the challenge server to solve the task:
> `nc shellcode.tghack.no 1111`
> Note: This is level 6. End your assembly code with a line containing EOF.

## Solution

We talked about the registers for function parameters earlier. We'll use those here.

Our assembly code is:
```
mov rax, rdi
mul rsi
ret
EOF
```

```
TG20{two_parameters!}
```