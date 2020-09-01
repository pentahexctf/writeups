ct = "aavhyp1x1t]e2pp_]e/x1]w2s]sr{"
ret = ""
for a in ct:
        if ord(a) % 2 == 0:
                ret += chr(ord(a) - 2)
        else:
                ret += chr(ord(a) + 2)
print(ret)
