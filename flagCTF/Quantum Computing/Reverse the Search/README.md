
# flagCTF – Reverse the Search

* **Category:** Quantum Computing
* **Points:** 50

## Challenge

> We tried running this graph coloring program to test our quantum programming skills on an IBM Q style quantum computer, but the results were a bit off. We narrowed it down to the oracle function replicated below. Someone said something that we need to perform uncomputation after we make our measurement so that we return the variable. What are the four lines that we need to add at the bottom here? Write them in all lowercase, with a semicolon after each statement including the final one, and with no spaces in any of the statements, on the same line.
>
> For example, you would submit "x+=1;print(x);" if you thought that was the answer.
> 
> ```
> def color_works(circuit, f_in, f_out, aux, n):
>     circuit.cx(f_in[2],aux[0])
>     circuit.cx(f_in[1],aux[0])
>     
>     circuit.cx(f_in[1],aux[1])
>     circuit.cx(f_in[0],aux[1])
>     
>     circuit.ccx(aux[0], aux[1], f_out[0])
> ```

## Solution

I honestly spent a lot more time than I should have on this challenge. Since the challenge asks us to uncompute, all we have to do is repeat the operations done. So, our code becomes:

```
def color_works(circuit, f_in, f_out, aux, n):
    circuit.cx(f_in[2],aux[0])
    circuit.cx(f_in[1],aux[0])
    
    circuit.cx(f_in[1],aux[1])
    circuit.cx(f_in[0],aux[1])
    
    circuit.ccx(aux[0], aux[1], f_out[0])

    circuit.cx(f_in[2],aux[0])
    circuit.cx(f_in[1],aux[0])
    
    circuit.cx(f_in[1],aux[1])
    circuit.cx(f_in[0],aux[1])
```

Take the newly added lines, and sort them alphabetically:

```
circuit.cx(f_in[0],aux[1]);circuit.cx(f_in[1],aux[0]);circuit.cx(f_in[1],aux[1]);circuit.cx(f_in[2],aux[0]);
```