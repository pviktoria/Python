import random

def genrandom():
	list=[]
	for i in range(0,5):
		number= random.randint(1,45)
		print(number)
		list.append(number)
		
	result= calcmiddle(list)
	print("Az átlag: {:<10.3f}".format(result))
	
def calcmiddle(list):
	
	result=0;
	counter=0;
	for i in list:
		result+= i
		counter+= 1
	
	resault= result/counter	
	return result

genrandom()
