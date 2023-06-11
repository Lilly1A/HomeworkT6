"""
Un utilizator va introduce un sir de numere, separate prin virgula de la consola.

Din sirul introdus creaza o lista de numere.

Afla suma elementelor pare si a celor impare din lista si afiseazo.
"""

sir=input('Intorduceti un sire de numere, separate prin virgula: ')

lista=list(sir.split(","))
print(lista)
lungimea=len(lista)

suma_pare=0
suma_impare=0

for numar in lista:
    numar=int(numar)
    if numar % 2 == 0:
        suma_pare+=numar
    else:
        suma_impare+=numar
print(f'Sumele numerelor pare este {suma_pare} si celor impare este {suma_impare}')





