import math
from base64 import b64decode

ct = "lYWJlYWJlcLFwcLFwcLFwcLFwcG^m^m^5e\\FwcLFwcLFwcLFsfG|sfLJ|Ono:Oi4xP\\FwcLFwcLFwcGxva6xva6xufm5ufrx7h3h3h3h3crNoaGloPi8uPmJlYWJlYWJxfW1xfy1~c3R~cLFwcLFgYGFgYHIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMrNycmhmj39/j39/j3<=YWJ"

def up(ct): # parity bs
    ret = ""
    for i in ct:
        if ord(i) % 2 == 0:
            ret += chr(ord(i) - 2)
        else:
            ret += chr(ord(i) + 2)
    return ret

def you(ct): # fix the shift + remove index
    ret = ""
    for i in range(len(ct)):
        ret += chr(ord(ct[(i - 3 + len(ct)) % len(ct)]) - 2)
    return ret

def give(ct): # bsae64 decode
    return b64decode(ct).decode()

def gonna(ct): # xor
    ret = ""
    for i in ct:
        ret += chr(ord(i) ^ 3)
    return ret

def never(ct): # subtract one from the charcode. skip the next n characters (as determined by the function stupid(), which is just copied and pasted)
    ret = ""
    i = 0
    j = 0
    while i < len(ct):
        ret += chr(ord(ct[i]) + 1)
        i += stupid(j)
        j += 1
    return ret

def stupid(x): # stupid
    return abs(int(4 + 2.3 * math.sin(x) + 0.8 * math.tan(2.3 * x)))


print(never(gonna(give(you(up(ct))))))
