
def  multinumber():
	list=[]

	for i in range(0,5):
		number=int(input("Szám: "))
		list.append(number)

	multiplenum=multiple(list)
	print("A szorzat: {:^10}".format(multiplenum))
		
def multiple(list ):

	sum= 1
	for i in list:
		sum*=i
	return sum

multinumber()
