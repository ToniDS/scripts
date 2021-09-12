#!/usr/bin/env python

"""
Baut die Funktion **snake_case** so, dass die Tests **True** ausgeben.
Macht es C-like in pure python ohne imports und ohne fancy string Methoden (Beispiel: kein lower, keine der Funktionen https://twitter.com/AbzAaron/status/1434556230014541826) (das join ist nur für die tests der Übersicht halber drin).
Da Python strings nicht by-ref übergeben kann und es mehr wie C sein soll wird mit Listen gearbeitet.
"""

# hand written C-like snake_case without fancy python methods


def snake_case(txt_ar):
    new_ar = txt_ar.copy()
    i = 0
    while i <= len(txt_ar) -1:
        print(new_ar)
        if 65 <= ord(txt_ar[i]) <= 90:
            new_ar[i] = "_"
            new_ar[i + 1] = chr(ord(txt_ar[i]) + 32)
            new_ar.append(" ")
            for j in range(i + 2, len(txt_ar) + 1):
                new_ar[j] = txt_ar[j - 1]
            txt_ar[:] = new_ar.copy()
            i += 1
        else:
            new_ar[i] = txt_ar[i]
            i += 1
    txt_ar[:] = new_ar
    while txt_ar[-1] == " ":
        txt_ar[:] = txt_ar[:-1]

# tests

char_ar = ['m', 'a', 'k', 'e', 'S', 'n', 'a', 'k', 'e', 'C', 'a', 's', 'e', ' ', ' ']
snake_case(char_ar)
print('# TEST 1: ', ''.join(char_ar) == "make_snake_case")
print('Output: ', ''.join(char_ar))  # Output: make_snake_case

char_ar = ['m', 'o', 'r', 'e', ' ', 'S', 'n', 'a', 'k', 'e', ' ']
snake_case(char_ar)
print('# TEST 2: ', ''.join(char_ar) == "more _snake")
print('Output: ', ''.join(char_ar))  # Output: more _snake

char_ar = ['B', 'l', 'e', 'r', 'g', 'h', ' ']
snake_case(char_ar)
print('# TEST 3: ', ''.join(char_ar) == "_blergh")
print('Output: ', ''.join(char_ar))  # Output: _blergh

char_ar = ['l', 'O', 'L', ' ', ' ']
snake_case(char_ar)
print('# TEST 4: ', ''.join(char_ar) == "l_o_l")
print('Output: ', ''.join(char_ar))  # Output: _blergh