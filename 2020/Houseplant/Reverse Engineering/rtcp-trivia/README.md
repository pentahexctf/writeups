# Houseplant CTF – RTCP Trivia

* **Category:** Reverse Engineering
* **Points:** 1882 Points

## Challenge

> We now have our very own trivia app! Solve 1000 questions and win a flag!
> 
> Dev: jammy

(client.apk was attached)

## Solution

This was an Android reversing challenge. The app connected via websockets to a server, which sent back and forth data to answer questions. To get the flag, you would need to answer 1000 questions correctly.

First thing I did was upload the .apk to [http://www.javadecompilers.com/apk](http://www.javadecompilers.com/apk), which decompiled the apk and gave me some readable Java source.

Opening `Game.java`, we see "AES/CBC/PKCS7Padding", which means that the server and client probably communicate through AES. Thankfully, the code to generate the key and IV has to be on the client somewhere, so if we can grab those values, we can use them to decrypt all the traffic.

To view the traffic, I used an Android emulator on my computer, and used Wireshark to inspect packets. Upon connecting to the server, a WebSocket connection is established to `ws://challs.houseplant.riceteacatpanda.wtf:40001`. All of the packets sent back and forth are bits of JSON data with a key named "method", which describes what type of packet.

First, an `ident` packet is sent, with a `userToken` that is generated by the client. The server sends back an `ident` packet with `success` set to true, which lets the user know it is connected. Then the user and server send back and forth a `start` packet to start the game. Once the game is started, the server will send a `question` packet with a question `id`, `requestIdentifier`, `questionText`, `options`, and `correctAnswer`. However, `questionText, `options`, and `correctAnswer` are all encrypted using AES CBC. Since the client can still read the question, the app must have the AES key and IV somewhere.

Checking the decompiled `Game.java`, we see this:

```java
JSONObject jSONObject = new JSONObject(this.f3310d);
String a = new C0784nx(Game.this.getIntent().getStringExtra("id"), Game.this.getResources()).mo2708a();
String string = jSONObject.getString("id");
StringBuilder sb = new StringBuilder();
sb.append(a);
sb.append(":");
sb.append(string);
byte[] a2 = C0784nx.m2603a(sb.toString());
byte[] b = C0784nx.m2604b(jSONObject.getString("requestIdentifier"));
SecretKeySpec secretKeySpec = new SecretKeySpec(a2, "AES");
IvParameterSpec ivParameterSpec = new IvParameterSpec(b);
``` 

The game generates a new key and IV on every question. It generates the `secretKeySpec` key based on the user's provided token and the id, but also used some methods in `C0784nx`, which I had to reverse next.

In `C0784nx.java`, we have methods that manipulate the data in some way to generate the key and IV. First, let's look at the key.

The key is generated using the `mo2708a` method, which also uses the `m2605c` method.
```java
private String m2605c(String str) {
    MessageDigest instance = MessageDigest.getInstance("SHA-256");
    StringBuilder sb = new StringBuilder();
    sb.append(str);
    sb.append(":");
    sb.append(this.f3315b);
    byte[] digest = instance.digest(new String(sb.toString()).getBytes());
    StringBuffer stringBuffer = new StringBuffer();
    for (byte b : digest) {
        String hexString = Integer.toHexString(255 & b);
        if (hexString.length() == 1) {
            stringBuffer.append('0');
        }
        stringBuffer.append(hexString);
    }
    return String.valueOf(stringBuffer);
}

/* renamed from: a */
public final String mo2708a() {
    InputStream openRawResource = this.f3314a.openRawResource(R.raw.correct);
    byte[] bArr = new byte[openRawResource.available()];
    byte[] bArr2 = new byte[openRawResource.available()];
    openRawResource.read(bArr);
    openRawResource.close();
    new ArrayList();
    for (int i = 0; i < bArr.length; i++) {
        double d = (double) i;
        if (Math.sqrt(d) % 1.0d == 0.0d) {
            bArr2[(int) Math.sqrt(d)] = bArr[i];
        }
    }
    byte[] digest = MessageDigest.getInstance("SHA-256").digest(bArr2);
    StringBuffer stringBuffer = new StringBuffer();
    for (byte b : digest) {
        String hexString = Integer.toHexString(255 & b);
        if (hexString.length() == 1) {
            stringBuffer.append('0');
        }
        stringBuffer.append(hexString);
    }
    return m2605c(String.valueOf(stringBuffer));
}
```

Because of the `openRawResource` call, I couldn't exactly reverse the function based on the Java alone. So, I used `apktool` to decompile the .apk into `.smali` code, and added Android log statements into the code. I then read the values printed to the log using `adb`.

Doing this led me to the realization that `stringBuffer` in `mo2708a` was the same every time, specifically "cbce23dfcdc7efe826d23bbf3d635d8fd55b6499d16ca8830a973ff57175119f". From there, I just had to reverse `m2605c("cbce23dfcdc7efe826d23bbf3d635d8fd55b6499d16ca8830a973ff57175119f")`.

`m2605c` obviously had some SHA-256 magic, but after that was some weird `Integer.tohexString` stuff. However, after doing the math, I realized that the SHA-256 hash did nothing. Huh. So, `m2605c` just returns the SHA-256 hash of the parameter, which we know, and `this.f3315b`, which is the userToken.

Now that that is reversed, we can go back to `Game.java`. After this call, the result of this SHA-256 hash is run through `m2603a` with the question id, which just turns out to be another SHA-256 hash.

So, the formula for the key is sha256(sha256(cbce23dfcdc7efe826d23bbf3d635d8fd55b6499d16ca8830a973ff57175119f:userToken):id)).

Now, to figure out the IV, I just logged the IV as it was passed into `IvParameterSpec`, and it turned out just to be the `requestIdentifier` given by data.

Now that both the key and IV are obtained, we can now decrypt the packets sent by the server! `questionText` and `options` are the questions and answers respectively, and `correctAnswer` is the number of the correct answer choice! Knowing this, we can assemble a Python script which will run through all 1000 questions.


```
rtcp{qu1z_4pps_4re_c00l_aeecfa13}
```