python
import sys
import math
import struct
import random
from z3 import *
import requests

MASK = 0xFFFFFFFFFFFFFFFF

def xs128p(state0, state1):
    s1 = state0 & MASK
    s0 = state1 & MASK
    s1 ^= (s1 << 23) & MASK
    s1 ^= (s1 >> 17) & MASK
    s1 ^= s0 & MASK
    s1 ^= (s0 >> 26) & MASK 
    state0 = state1 & MASK
    state1 = s1 & MASK
    generated = state0 & MASK

    return state0, state1, generated

def sym_xs128p(slvr, sym_state0, sym_state1, generated):
    s1 = sym_state0 
    s0 = sym_state1 
    s1 ^= (s1 << 23)
    s1 ^= LShR(s1, 17)
    s1 ^= s0
    s1 ^= LShR(s0, 26) 
    sym_state0 = sym_state1
    sym_state1 = s1
    calc = sym_state0
    
    condition = Bool('c%d' % int(generated * random.random()))
    impl = Implies(condition, LShR(calc, 12) == int(generated))
    
    slvr.add(impl)
    return sym_state0, sym_state1, [condition]

def reverse17(val):
    return val ^ (val >> 17) ^ (val >> 34) ^ (val >> 51)

def reverse23(val):
    return (val ^ (val << 23) ^ (val << 46)) & MASK

def xs128p_backward(state0, state1):
    prev_state1 = state0
    prev_state0 = state1 ^ (state0 >> 26)
    prev_state0 = prev_state0 ^ state0
    prev_state0 = reverse17(prev_state0)
    prev_state0 = reverse23(prev_state0)
    generated = prev_state0
    
    return prev_state0, prev_state1, generated

def to_double(out):
    double_bits = (out >> 12) | 0x3FF0000000000000
    double = struct.unpack('d', struct.pack('<Q', double_bits))[0] - 1
    return double

def main():
    req = requests.post("http://challs.houseplant.riceteacatpanda.wtf:30006/guess", json=[1,2,3,4,5])
    dubs = []
    for v in req.json()['results']:
        dubs.append(v/1000)
    print('initial numbers', dubs)

    dubs = dubs[::-1]
    generated = []
    for idx in range(len(dubs)):
        recovered = struct.unpack('<Q', struct.pack('d', dubs[idx] + 1))[0] & (MASK >> 12)
        generated.append(recovered)

    ostate0, ostate1 = BitVecs('ostate0 ostate1', 64)
    sym_state0 = ostate0
    sym_state1 = ostate1
    slvr = Solver()
    conditions = []

    for ea in range(len(dubs)):
        sym_state0, sym_state1, ret_conditions = sym_xs128p(slvr, sym_state0, sym_state1, generated[ea])
        conditions += ret_conditions

    if slvr.check(conditions) == sat:
        m = slvr.model()
        state0 = m[ostate0].as_long()
        state1 = m[ostate1].as_long()
        slvr.add(Or(ostate0 != m[ostate0], ostate1 != m[ostate1]))
        if slvr.check(conditions) == sat:
            print('WARNING: multiple solutions found! use more dubs!')

        generated = []
        for idx in range(500):
            state0, state1, out = xs128p_backward(state0, state1)
            out = state0 & MASK

            double = to_double(out)
            generated.append(double)

        req2 = requests.post("http://challs.houseplant.riceteacatpanda.wtf:30006/guess", json=[1,2,3,4,5])
        dubs2 = []
        for v in req2.json()['results']:
            dubs2.append(v/1000)
        print('marker numbers', dubs2)

        last = dubs2[-1]
        start = generated.index(last)

        answer = []
        answer.append(math.floor(generated[start+1]*1000))
        answer.append(math.floor(generated[start+2]*1000))
        answer.append(math.floor(generated[start+3]*1000))
        answer.append(math.floor(generated[start+4]*1000))
        answer.append(math.floor(generated[start+5]*1000))

        print('final answer', answer)

        final = requests.post("http://challs.houseplant.riceteacatpanda.wtf:30006/guess", json=answer)
        print(final.text)
    else:
        print('unsolvable')

main()