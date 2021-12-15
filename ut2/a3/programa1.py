import sys
n=int(sys.argv[1])
esPrimo=True
for i in range(2,n):
	if n%i==0:
		esPrimo=False
		break
if n <=0:
	print ("Debe introducir un número positivo")
elif esPrimo:
	print ("Es un número primo")
else:
	print ("No es un número primo")
