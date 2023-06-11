"""

Calculator BMI
Scrie un program care primește greutatea unei persoane (în kilograme) și înălțimea (în metri)
a intrare și calculează Indicele de Masă Corporală (BMI). Apoi clasifică BMI-ul în următoarele categorii:
Subponderal (BMI < 18,5)
Greutate normală (BMI între 18,5 și 24,9)
Supraponderal (BMI între 25 și 29,9)
Obezitate (BMI 30 sau mai mare)
Pentru a calcula Indicele de Masă Corporală (BMI), urmează pașii de mai jos:
1. Ia greutatea persoanei în kilograme și înălțimea în metri.
2. Calculează pătratul înălțimii (înmulțește înălțimea cu ea însăși).
3. Calculează BMI-ul utilizând formula: BMI = greutate / înălțime^2, unde greutatea este
în kilograme și înălțimea este în metri.
4. Rezultatul obținut va fi indicele de masă corporală al persoanei.

"""
greutatea = int(input('Introduceti greutatea in kg: '))
inaltimea = float(input('Introduceti inaltimea in metri: '))

bmi=round(greutatea/inaltimea**2,2)
print('BMI este ', bmi)
if bmi >= 30:
    print('Obezitate')
elif 25 <= bmi <= 29.9:
    print('Supraponderal')
elif 18.5 <= bmi <= 24.9:
    print('Greutate normala')
else:
    print('Subponderal')