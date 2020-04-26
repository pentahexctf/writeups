skats = {"L": "ㄱ", "F": "ㄴ", "B": "ㄷ", "V": "ㄹ", "M": "ㅁ", "W": "ㅂ", "G": "ㅅ", "K": "ㅇ", "P": "ㅈ", "C": "ㅊ", "X": "ㅋ", "Z": "ㅌ", "O": "ㅍ", "J": "ㅎ", "E": "ㅏ", "I": "ㅑ", "T": "ㅓ", "S": "ㅕ", "A": "ㅗ", "N": "ㅛ", "H": "ㅜ", "R": "ㅠ", "D": "ㅡ", "U": "ㅣ", "TU": "ㅔ", "EU": "ㅐ", "SU": "ㅖ", "IU": "ㅒ"}

decode = "JDU MEK KDF PUF PTK JEF LU GEUK CHK KUW FU BE"

decode = decode.split(" ")

for i in decode:
    arr = []
    for j in i:
        arr.append(skats[j])
    print("".join(arr))
