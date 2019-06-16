# flagCTF – Exquisifax Admin Panel

* **Category:** Quantum Computing
* **Points:** 50

## Challenge

>Challenge text here
>lol

## Solution

I don't really know what to write here, the challenge was mostly logic.

The ccccx operation is essentially just the and operation with 4 parameters, which is just ```and(and(a, b), (c, d))```.

To do that with ccx gates, we need to use the auxiliary variables. So, to do ```and(controls[0], controls[1])``` we just do ```ccx(controls[0], controls[1], aux[0])``` and to do ```and(controls[2], controls[3])``` we just do ```ccx(controls[2], controls[3], aux[1])```. Then, to compare the results of the two, we do ```ccx(aux[0], aux[1], target```.

Don't forget to uncompute! All you have to do is repeat the first two operations. The final code is:

```
ccx(controls[0], controls[1], aux[0])
ccx(controls[2], controls[3], aux[1])
ccx(aux[0], aux[1], target)
ccx(controls[0], controls[1], aux[0])
ccx(controls[2], controls[3], aux[1])
```

This makes a minimum of 5 lines, with the fourth line of code being ```ccx(controls[0], controls[1], aux[0])```.

```
5;circuit.ccx(controls[0],controls[1],aux[0])
```

Note: The regex to match the flag was not working, so we were instead directed to submit the following flag:

```
638433291152a52e7b4e8c7ad09e93a3
```