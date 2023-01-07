from libraries import *
t = Timer()

# t.print_time_elapse('started program')

# t.print_time_elapse("loaded libraries")

label = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z", "cipher_type"]

dataset = read_csv("training_data.csv", names=label)

# Split-out validation dataset
array = dataset.values
X = array[:, 0:26]
y = array[:, 26]
X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1)

model = LogisticRegression(solver='liblinear', multi_class='ovr')
model.fit(X_train, Y_train)
predictions = model.predict(X_validation)

# t.print_time_elapse("training done")

ciphertext = input("ciphertext: ")
frequencies = get_frequency_data(ciphertext)

print("\n" + str(frequencies))

if model.predict([frequencies]) == ['r']:
    print("ROT13\n")
    p = []
    c = ciphertext.split(" ")
    for word in c:
        plain = []
        letters = list(word)
        for char in letters:
            char = char.lower()
            if atbash.get(char) is not None:
                pl = rot13.get(char)
            else:
                pl = char
            plain.append(pl)
        p.append("".join(plain))
    print(" ".join(p).upper())

elif model.predict([frequencies]) == ['a']:
    print("Atbash\n")
    p = []
    c = ciphertext.split(" ")
    for word in c:
        plain = []
        letters = list(word)
        for char in letters:
            char = char.lower()
            if atbash.get(char) is not None:
                pl = atbash.get(char)
            else:
                pl = char
            plain.append(pl)
        p.append("".join(plain))
    print(" ".join(p).upper())

elif model.predict([frequencies]) == ['c']:
    print("Caesar\n")
    p = []
    c = ciphertext.split(" ")
    for word in c:
        plain = []
        letters = list(word)
        for char in letters:
            char = char.lower()
            if char in caesar:
                for ch in caesar:
                    if caesar[ch] == char:
                        pl = ch
            else:
                pl = char
            plain.append(pl)
        p.append("".join(plain))
    print(" ".join(p).upper())

# t.print_time_elapse("finished")
