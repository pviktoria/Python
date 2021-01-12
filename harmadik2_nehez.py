Név= 'Pap Viktória, '
Osztály= 'Szoftverfejlesztő-esti, '
Dátum= '2020-12-16,  15m'
Feladat='Állatok nevét és súlyát adja meg'
print(Név, Dátum)
print(Feladat)

import allat

állatfajok = []

for _ in range(3):
    fajnév = input('Add meg egy állatfaj nevét! ')
    tömeg = input('Hány kilogramm a tömege egy példánynak? ')
    állatfaj = allat.Állatfaj(fajnév, tömeg)
    állatfajok.append(állatfaj)

legnehezebb_állat = állatfajok[0]

for állatfaj in állatfajok:
    print('A(z) ', állatfaj.fajnév, ' tömege ', állatfaj.tömeg, ' kg.', sep='')
    if állatfaj.tömeg > legnehezebb_állat.tömeg:
       legnehezebb_állat = állatfaj
    
célfájl = open('legnehezebb.txt', 'w')
print('A(z)', legnehezebb_állat.fajnév, 'a legnehezebb.', file=célfájl)
célfájl.close()
