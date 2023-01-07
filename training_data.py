from nltk.corpus import words
import random
from utility import *

words_list = words.words()

common_words = []

with open("1-1000.txt", "r") as c:
    for line in c:
        line = line.strip()
        common_words.append(line)
t = open("training_data.txt", "w")

# atbash
for i in range(0, 1000):
    plaintext_len = random.randint(1, 40)
    plaintext = []
    ciphertext = []
    random_location = random.randint(0, plaintext_len)
    for word_n in range(0, plaintext_len):
        if word_n == random_location or word_n == random_location * 2:
            plain_word = random.choice(words_list).lower()
        else:
            plain_word = random.choice(common_words).lower()
        letters = list(plain_word)
        print(letters)
        if "'" in letters:
            letters.remove("'")
        if "-" in letters:
            letters.remove("-")
        cipher_letters = []
        for letter in letters:
            cipher_letter = atbash.get(letter)
            cipher_letters.append(cipher_letter)
        print(cipher_letters)
        cipher_word = "".join(cipher_letters)
        ciphertext.append(cipher_word)

    t.write("a," + " ".join(ciphertext) + "\n")

# rot13
for i in range(0, 1000):
    plaintext_len = random.randint(1, 40)
    plaintext = []
    ciphertext = []
    random_location = random.randint(0, plaintext_len)
    for word_n in range(0, plaintext_len):
        if word_n == random_location or word_n == random_location * 2:
            plain_word = random.choice(words_list).lower()
        else:
            plain_word = random.choice(common_words).lower()
        letters = list(plain_word)
        print(letters)
        if "'" in letters:
            letters.remove("'")
        if "-" in letters:
            letters.remove("-")
        cipher_letters = []
        for letter in letters:
            cipher_letter = rot13.get(letter)
            cipher_letters.append(cipher_letter)
        print(cipher_letters)
        cipher_word = "".join(cipher_letters)
        ciphertext.append(cipher_word)

    t.write("r," + " ".join(ciphertext) + "\n")

# caesar
for i in range(0, 1000):
    plaintext_len = random.randint(1, 40)
    plaintext = []
    ciphertext = []
    random_location = random.randint(0, plaintext_len)
    for word_n in range(0, plaintext_len):
        if word_n == random_location or word_n == random_location * 2:
            plain_word = random.choice(words_list).lower()
        else:
            plain_word = random.choice(common_words).lower()
        letters = list(plain_word)
        print(letters)
        if "'" in letters:
            letters.remove("'")
        if "-" in letters:
            letters.remove("-")
        cipher_letters = []
        for letter in letters:
            cipher_letter = caesar.get(letter)
            cipher_letters.append(cipher_letter)
        print(cipher_letters)
        cipher_word = "".join(cipher_letters)
        ciphertext.append(cipher_word)

    t.write("c," + " ".join(ciphertext) + "\n")
