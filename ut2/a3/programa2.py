import sys
n=int(sys.argv[1])
suma=0
for i in range (1,n+1):
	cuadrado=i*i
	suma= suma + cuadrado

if n <=0:
	print ("Debe introducir un número positivo")

else:
	print (suma)
