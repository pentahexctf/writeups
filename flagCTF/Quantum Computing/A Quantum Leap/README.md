# flagCTF – Quantum Leap

* **Category:** Quantum Computing
* **Points:** 50

## Challenge

> Note: if you obtained a flag from the admins you can enter it as well.
> 
> Gate-based quantum computing requires reversible computation -- that the inputs at the beginning of the circuit can be deduced from the outputs of the end of the circuit. For the purposes of this problem, you can take this property for granted. So, with a NOT gate, output 0 came from input 1, and output 1 came from input 0. However, where we might use an AND circuit in classical computing, it would not be possible to work backwards -- output 1 came from input 1,1, but did output 0 come from input 0,0, 0,1, or 1,0? Quantum programs instead use reversible gates. One such reversible gate is a controlled not (CX) gate. A CX gate leaves the first ("control") input the same, and iff the first input is a 1, flips the second input. It's easy to undo this operation -- its reverse is just itself! If the first input was 0, no change is ever made, and if the first input was 1, it undoes the change. These gates can also be used in classical computing as well.
> 
> Similar to a CX gate is a CCX gate. This flips the third input iff the first two inputs are both 1. This is the closest we get to an AND gate in quantum computing -- it's reversible, because it keeps the first two inputs the same, and flips the third input if both controls are 1, rather than overwriting it outright. The CCX gate's reverse is again itself.
> 
> There is a restriction that each qubit in a gate must be distinct. Qubits cannot be cloned to be used as other inputs (due to the No Cloning Theorem), nor can the input of a gate be used as the output of that same gate, as we might do on a traditional computer with "x = x AND y". So, there may be a need for auxiliary qubits (for example: z = x AND y; x = z). Note that the assignment target is on the right.
> 
> Here we use the first qubit in a length-2 array of auxiliary qubits, aux, to make the CCCX gate on the first 3 elements of controls, storing the answer in target.
> 
> circuit.ccx(controls[0],controls[1],aux[0])
> circuit.ccx(controls[2],aux[0],target)
> circuit.ccx(controls[0],controls[1],aux[0])
> You have been tasked with editing this code to implement a CCCCX gate using 2 auxiliary qubits, with 4 controls, using the least number of statements possible. What is that minimal number, and what is the 4th statement in your implementation? The flag is your answers separated by a semicolon, with no spaces in the flag. If you believe you have a correct answer that is not being accepted, PM one of the admins on Slack.

## Solution

I don't really know what to write here, the challenge was mostly logic.

The ccccx operation is essentially just the ```and``` operation with 4 parameters, which is just ```and(and(a, b), and(c, d))```.

To do that with ccx gates, we need to use the auxiliary variables. So, we just do ```ccx(controls[0], controls[1], aux[0])``` and ```ccx(controls[2], controls[3], aux[1])```. Then, to compare the results of the two, we do ```ccx(aux[0], aux[1], target)```.

Don't forget to uncompute! All you have to do is repeat the first two operations. The final code is:

```
circuit.ccx(controls[0], controls[1], aux[0])
circuit.ccx(controls[2], controls[3], aux[1])
circuit.ccx(aux[0], aux[1], target)
circuit.ccx(controls[0], controls[1], aux[0])
circuit.ccx(controls[2], controls[3], aux[1])
```

This makes a minimum of 5 lines, with the fourth line of code being ```ccx(controls[0], controls[1], aux[0])```.

```
5;circuit.ccx(controls[0],controls[1],aux[0])
```

Note: The regex to match the flag was not working, so we were instead directed to submit the following flag:

```
638433291152a52e7b4e8c7ad09e93a3
```