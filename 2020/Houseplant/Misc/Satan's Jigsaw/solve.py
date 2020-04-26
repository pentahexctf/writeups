from PIL import Image
from Crypto.Util.number import long_to_bytes
from os import listdir
from os.path import isfile, join


im2 = Image.new('RGB', (300, 300))
pix = im2.load()

path = "chall/"

onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

print("Loaded files.")

for i in onlyfiles:
    im = Image.open("chall/" + i)
    long = int(i.split(".")[0])
    a = [ int(i) for i in long_to_bytes(long).decode().split(" ") ]
    x, y = a[0], a[1]
    #print(x, y)
    pix[x, y] = im.getpixel((0, 0))

im2.save("solved.png")
