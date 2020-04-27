#! /usr/bin/env python3
from qrtools.qrtools import QR
import requests

qr = QR()
a = "`head -c 200 flag.txt | tail -c 200`"
b = f"{1 + 2}"
