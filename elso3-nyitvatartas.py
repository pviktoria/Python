Név= 'Pap Viktória, '
Osztály= 'Szoftverfejlesztő-esti, '
Dátum= '2020-12-16,  15m'
Feladat='Megállapítja, mennyi idő van a bolt zárásáig'
print(Név, Dátum)
print(Feladat)

óra = input('Hány óra van most? ')
óra = int(óra)
if óra >= 8 and óra < 16:
    print('A bolt nyitva van.')
    még_ennyit_van_nyitva = 16 - óra
    print('Ennyi órád van még odaérni:', még_ennyit_van_nyitva)
else:
    print('A bolt zárva van.')
