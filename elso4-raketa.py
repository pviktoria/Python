Név= 'Pap Viktória, '
Osztály= 'Szoftverfejlesztő-esti, '
Dátum= '2020-12-16,  15m'
Feladat='Rakéta indulását méri időben'
print(Név, Dátum)
print(Feladat)

indul = input('Hány órás visszaszámlálást tervezünk? ')
indul = int(indul)

felfüggesztések = 0

for szám in range(indul, 0, -1):
    print('Visszaszámlálás:', szám)
    válasz = input('Fel kell függeszteni a visszaszámlálást (i/n)? ')
    if válasz == 'i':
        felfüggesztések += 1

print('A rakéta a visszaszámlálást követően ennyi órával indult:', indul + felfüggesztések)
