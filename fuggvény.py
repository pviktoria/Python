#bekér 3 számot, 
import math

def base():
	
	numbers=[]

	for i in range(0,3):
		number= int(input("Kérek egy számot: ")) # 3x kér be számot
		numbers.append(number) # itt tárolja, de nem írja ki
		
	result=calculate(numbers)
	print(result)
	
def calculate(numbers):
	sum= 0
	for szam in range (len(numbers)):
		sum+=math.pow(numbers[szam], 2)
	
	return sum

base()
