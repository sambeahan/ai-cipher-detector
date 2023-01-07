from utility import caesar

p = []

ciphertext = input("Enter ciphertext: ")
c = ciphertext.split(" ")
for word in c:
    plain = []
    letters = list(word)
    for char in letters:
        char = char.lower()
        if char in caesar:
            pl = caesar[char]
        else:
            pl = char
        plain.append(pl)
    p.append("".join(plain))
print(" ".join(p).upper())