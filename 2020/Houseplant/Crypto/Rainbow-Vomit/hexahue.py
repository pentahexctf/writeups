from PIL import Image

img = input("Enter the image filename:")
img = Image.open(img)

w,h = img.size

#convert image to RGBCYPWBkG
colormarker = {
	"R":(255,0,0),
	"G":(0,255,0),
	"B":(0,0,255),
	"C":(0,255,255),
	"P":(255,0,255),
	"Y":(255,255,0),
	"W":(255,255,255),
	"Bl":(0,0,0),
	"Gr":(128,128,128)
}

newimg = []
for y in range(h):
	newrow = []
	for x in range(w):
		currpixel = img.getpixel((x,y))
		for key,value in colormarker.items():
			#print("Checking {}...".format(key))
			if currpixel == value:
				#print("Success. Worked: {}".format(key))
				newrow += [key]
				break
	newimg += [newrow]
#print(newimg)

#translate from hexahue.

hexahue = {
	"A":[["P","R"],["G","Y"],["B","C"]],
	"B":[["R","P"],["G","Y"],["B","C"]],
	"C":[["R","G"],["P","Y"],["B","C"]],
	"D":[["R","G"],["Y","P"],["B","C"]],
	"E":[["R","G"],["Y","B"],["P","C"]],
	"F":[["R","G"],["Y","B"],["C","P"]],
	"G":[["G","R"],["Y","B"],["C","P"]],
	"H":[["G","Y"],["R","B"],["C","P"]],
	"I":[["G","Y"],["B","R"],["C","P"]],
	"J":[["G","Y"],["B","C"],["R","P"]],
	"K":[["G","Y"],["B","C"],["P","R"]],
	"L":[["Y","G"],["B","C"],["P","R"]],
	"M":[["Y","B"],["G","C"],["P","R"]],
	"N":[["Y","B"],["C","G"],["P","R"]],
	"O":[["Y","B"],["C","P"],["G","R"]],
	"P":[["Y","B"],["C","P"],["R","G"]],
	"Q":[["B","Y"],["C","P"],["R","G"]],
	"R":[["B","C"],["Y","P"],["R","G"]],
	"S":[["B","C"],["P","Y"],["R","G"]],
	"T":[["B","C"],["P","R"],["Y","G"]],
	"U":[["B","C"],["P","R"],["G","Y"]],
	"V":[["C","B"],["P","R"],["G","Y"]],
	"W":[["C","P"],["B","R"],["G","Y"]],
	"X":[["C","P"],["R","B"],["G","Y"]],
	"Y":[["C","P"],["R","G"],["B","Y"]],
	"Z":[["C","P"],["R","G"],["Y","B"]],
	".":[["Bl","W"],["W","Bl"],["Bl","W"]],
	",":[["W","Bl"],["Bl","W"],["W","Bl"]],
	" ":[["W","W"],["W","W"],["W","W"]],
	" ":[["Bl","Bl"],["Bl","Bl"],["Bl","Bl"]],
	"0":[["Bl","Gr"],["W","Bl"],["Gr","W"]],
	"1":[["Gr","Bl"],["W","Bl"],["Gr","W"]],
	"2":[["Gr","W"],["Bl","Bl"],["Gr","W"]],
	"3":[["Gr","W"],["Bl","Gr"],["Bl","W"]],
	"4":[["Gr","W"],["Bl","Gr"],["W","Bl"]],
	"5":[["W","Gr"],["Bl","Gr"],["W","Bl"]],
	"6":[["W","Bl"],["Gr","Gr"],["W","Bl"]],
	"7":[["W","Bl"],["Gr","W"],["Gr","Bl"]],
	"8":[["W","Bl"],["Gr","W"],["Bl","Gr"]],
	"9":[["Bl","W"],["Gr","W"],["Bl","Gr"]],
}

ptext = ""
for y in range(len(newimg))[::3]:
	for x in range(len(newimg[0]))[::2]:
		currgrid = []
		for i in range(y, y+3):
			currgrid += [newimg[i][x:x+2]]
		for key,value in hexahue.items():
			if value == currgrid:
				ptext += key
				break
print(ptext)

