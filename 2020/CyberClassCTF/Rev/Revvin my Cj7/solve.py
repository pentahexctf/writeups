ct = "c}tn{bLyp11pyLf_07ppt1_f0fkc"
halfOne = ct[::2]
halfTwo = ct[-1::-2]
ret = ""
for a, b in zip(halfOne, halfTwo):
	ret += a + b
print(ret)
