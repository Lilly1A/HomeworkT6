# Improve the password generator
"""
Inbunatatiti acest generator de parole, astfel in cat sa fie posibil sa genereze parole ce contin atat litere,
 cat si cifre si caractere speciale.
"""

import string
import random


all_letters =list(string.ascii_letters)
all_numbers = list(string.digits)
caractere_speciale = list(string.punctuation)

rezultat = all_letters + all_numbers + caractere_speciale

lungime = int(input('Introdu lungimea: '))

password = ''
for a in range(lungime):
    pozitie = random.randrange(0, len(rezultat))
    password += rezultat[pozitie]

print('Parola generata este', password)