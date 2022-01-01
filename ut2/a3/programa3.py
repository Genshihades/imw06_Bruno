
import sys

a=int(sys.argv[1])
b=int(sys.argv[2])

if a <=0 or b <=0:
	print ("Debe introducir números positivos")

def frac(a,b):
	return (a/b) - int(a/b)
def mcd(a,b):
	maximo=1
	for i in range(1,min(a,b)+1):
		if frac(a,i)<1e-9 and frac(b,i)<1e-9:
			maximo=i
	return maximo
print ("El máximo común divisor de {} y {} es: {}".format(a,b,mcd(a,b)))
