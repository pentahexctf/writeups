import json
import base64
import asyncio
import websockets
import hashlib
import binascii

from Crypto.Cipher import AES

BS = 16
def pad(s):
    return s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
def unpad(s):
    return s[0:-s[-1]]

class AESCipher:
    def __init__( self, key, iv):
        self.key = key
        self.iv = iv

    def encrypt( self, raw ):
        raw = pad(raw)
        cipher = AES.new( self.key, AES.MODE_CBC, self.iv )
        return base64.b64encode( self.iv + cipher.encrypt( raw ) )

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv )
        return unpad(cipher.decrypt(enc))

url = "ws://challs.houseplant.riceteacatpanda.wtf:40001"
userToken = "58e6384234e53bb09799556a2df8443ee4f0cb3274db5800855026c3ca2d3e4a"

def sha256(plaintext):
        m = hashlib.sha256()
        m.update(plaintext.encode("utf-8"))
        return m.hexdigest()

async def run():
        question = 1

        async with websockets.connect(url) as websocket:
                await websocket.send(json.dumps({
                        "method": "ident",
                        "userToken": userToken
                }))
                resp = json.loads(await websocket.recv())

                if resp["method"] == "ident" and resp["success"] == True:
                        print("Logged in successfully!")
                        print("Starting the game...")

                        await websocket.send(json.dumps({
                                "method": "start"
                        }))

                        resp = json.loads(await websocket.recv())
                        if resp["method"] == "start" and resp["success"] == True:
                                print("The game has started!")

                                while True:
                                        data = json.loads(await websocket.recv())
                                        if data["method"] == "question":
                                                id = data["id"]
                                                iv = data["requestIdentifier"]
                                                questionText = data["questionText"]
                                                answer = data["correctAnswer"]

                                                k1 = sha256(f"cbce23dfcdc7efe826d23bbf3d635d8fd55b6499d16ca8830a973ff57175119f:{userToken}")
                                                key = sha256(f"{k1}:{id}")

                                                cipher = AESCipher(bytes.fromhex(key), bytes.fromhex(iv))
                                                print(f"Question {question}: {cipher.decrypt(questionText).decode('utf-8')}")

                                                options = [cipher.decrypt(o).decode("utf-8") for o in data["options"]]
                                                for choice in options:
                                                        print(f"\t{choice}")

                                                answer = int(cipher.decrypt(answer))
                                                print(f"\tCorrect Answer: {options[answer]}")

                                                await websocket.send(json.dumps({
                                                        "method": "answer",
                                                        "answer": answer
                                                }))

                                                print("\n----\n")

                                                question += 1
                                        else:
                                                print(data)
                                                break


asyncio.get_event_loop().run_until_complete(run())