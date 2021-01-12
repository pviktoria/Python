Név= 'Pap Viktória, '
Osztály= 'Szoftverfejlesztő-esti, '
Dátum= '2020-12-16,  15m'
Feladat='Ágazati 001 mintafeladat megoldása'
print(Név, Dátum)
print(Feladat)
"""
print("Csapadék mennyiség miliméterben:")

aktuális= int(input("Aktuális heti csapadék: "))
előző= int(input("Előző heti csapadék: "))

if aktuális > előző:
	print("Több csapadék")
elif aktuális < előző:
	print("Kevesebb csapadék")
else:
	print("Azonos mennyiségű csapadék")
	
print("Szombathelyen mért hőmérséklet az elmúlt napokban:")

def fagy(fok):
    if fok <= 0:
        return True
    else:
        return False

napok= None 

while napok != '':
        fok = int(input('Adj meg egy hőmérsékletet: '))
        if fagy(fok):
            print('fagy volt.')
        else:
            print('fagy nem volt.')

"""           
        
from jarmu import Jarmu
 
class Eladas:
    def beolvas(self):
        self.jarmuvek = []
        fp = open('jarmu.txt', 'r')
        lines = fp.readlines()        
        for line in lines[1:]:            
            (az, rendszam, szin, marka, ar) = line.rstrip().split(':')
            jarmu = Jarmu(az, rendszam, szin, marka, int(ar))
            self.jarmuvek.append(jarmu)
        fp.close()
 
    def feher(self):
        feherek = 0
        for jarmu in self.jarmuvek:
            if jarmu.szin == 'fehér':
                feherek += 1 
        print('Fehérek:', feherek)
 
    def olcso(self):
        print('Olcsók:')
        for jarmu in self.jarmuvek:
            if jarmu.ar < 1000000:
                print(jarmu.rendszam, jarmu.szin, jarmu.ar);
 
    def feherOlcso(self):
        print('Fehér olcsók:')
        for jarmu in self.jarmuvek:
            if jarmu.ar < 1000000 and jarmu.szin == 'fehér':
                print(jarmu.rendszam, jarmu.szin, jarmu.ar);
 
eladas = Eladas()
eladas.beolvas()
eladas.feher()
eladas.olcso()
eladas.feherOlcso()

