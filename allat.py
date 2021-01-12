

class Állatfaj:
    def __init__(self, fajnév, tömeg):
        self.fajnév = fajnév
        self.tömeg = tömeg

összesállat=[]

for _ in range(3):
	fajnév=input("Add meg egy állatfaj nevét: ")
	tömeg=int(input("Hány kilógramm a tömege egy példánynal: "))
	állatfaj=fajnév, tömeg
	összesállat.append(állatfaj)

célfájl=open("legnehezebb.txt", "w")
print("A(z)", legnehezebb_állat.fajnév, 'a legnehezebb', file=célfájl")
célfájl.close

