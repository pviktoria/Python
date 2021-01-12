Név= 'Pap Viktória, '
Osztály= 'Szoftverfejlesztő-esti, '
Dátum= '2020-12-16,  15m'
Feladat='Felhasználónév és jelsző helyességét ellenőrzi'
print(Név, Dátum)
print(Feladat)

bejutott = False

while not bejutott:
    felhasználónév = input('Adja meg a felhasználónevét! ')
    jelszó = input('Adja meg a jelszavát! ')
    if felhasználónév == 'bori99' and jelszó == 'Szivecske<3':
        print('Belépés engedélyezve.')
        bejutott = True
    else:
        print('Belépés megtagadva.')
