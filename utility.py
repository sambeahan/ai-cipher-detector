import string
import numpy


def get_frequency_data(ciphertext, type=None):
    # take AABC as input and return [2,1,1,0,0,0,0,0,0,0,0,0,...0]
    ciphertext = ciphertext.replace(" ", "")
    frequency = []
    for i in range(26):
        frequency.append(0)
    for c in ciphertext:
        n = letter_position(c)
        frequency[n - 1] += 1

    if type:
        frequency.append(type)
    return frequency


def convert_list_of_lists_to_nparray(x):
    y = numpy.array([numpy.array(xi) for xi in x])
    return y


def letter_position(letter):
    ucase = string.ascii_uppercase
    pos = ucase.find(letter.upper()) + 1
    return pos

import time as time2
class Timer():
    def __init__(self):

        self.start_time = time2.time()

    def print_time_elapse(self, msg=''):
        delta_time = time2.time() - self.start_time
        print(delta_time, msg)
        self.start_time = time2.time()

atbash = {
    "a": "z",
    "b": "y",
    "c": "x",
    "d": "w",
    "e": "v",
    "f": "u",
    "g": "t",
    "h": "s",
    "i": "r",
    "j": "q",
    "k": "p",
    "l": "o",
    "m": "n",
    "n": "m",
    "o": "l",
    "p": "k",
    "q": "j",
    "r": "i",
    "s": "h",
    "t": "g",
    "u": "f",
    "v": "e",
    "w": "d",
    "x": "c",
    "y": "b",
    "z": "a"
}

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

rot13 = {
    "a": "n",
    "b": "o",
    "c": "p",
    "d": "q",
    "e": "r",
    "f": "s",
    "g": "t",
    "h": "u",
    "i": "v",
    "j": "w",
    "k": "x",
    "l": "y",
    "m": "z",
    "n": "a",
    "o": "b",
    "p": "c",
    "q": "d",
    "r": "e",
    "s": "f",
    "t": "g",
    "u": "h",
    "v": "i",
    "w": "j",
    "x": "k",
    "y": "l",
    "z": "m"
}

caesar = {
    "a": "d",
    "b": "e",
    "c": "f",
    "d": "g",
    "e": "h",
    "f": "i",
    "g": "j",
    "h": "k",
    "i": "l",
    "j": "m",
    "k": "n",
    "l": "o",
    "m": "p",
    "n": "q",
    "o": "r",
    "p": "s",
    "q": "t",
    "r": "u",
    "s": "v",
    "t": "w",
    "u": "x",
    "v": "y",
    "w": "z",
    "x": "a",
    "y": "b",
    "z": "c"
}

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

number_to_letter = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e',
    6: 'f',
    7: 'g',
    8: 'h',
    9: 'i',
    10: 'j',
    11: 'k',
    12: 'l',
    13: 'm',
    14: 'n',
    15: 'o',
    16: 'p',
    17: 'q',
    18: 'r',
    19: 's',
    20: 't',
    21: 'u',
    22: 'v',
    23: 'w',
    24: 'x',
    25: 'y',
    0: 'z'
}

p_number_to_letter = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e',
    6: 'f',
    7: 'g',
    8: 'h',
    9: 'i',
    10: 'j',
    11: 'k',
    12: 'l',
    13: 'm',
    14: 'n',
    15: 'o',
    16: 'p',
    17: 'q',
    18: 'r',
    19: 's',
    20: 't',
    21: 'u',
    22: 'v',
    23: 'w',
    24: 'x',
    25: 'y',
    26: 'z',
    27: '.',
    28: ',',
    29: '?',
    30: "'",
    31: '-',
    0: '"',
}


def let_to_num(letter):
    for n in number_to_letter:
        if number_to_letter[n] == letter:
            number = n
    return number


def num_to_let(number):
    return number_to_letter[number]


def p_let_to_num(letter):
    for n in p_number_to_letter:
        if p_number_to_letter[n] == letter:
            number = n
    return number


def p_num_to_let(number):
    return p_number_to_letter[number]