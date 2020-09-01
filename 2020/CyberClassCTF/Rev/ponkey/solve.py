ct = "ba`_ba`_srqpedcbzyxwonmlnmlkmlkjjihg210/xwvuLKJI3210MLKJ|{zy"
ct = ct[::4]
ret = ""
for a in ct:
	ret += chr(ord(a) + 1)
print(ret)
