from math import sqrt
import sys
a = float(input('psmax = '))
b = float(input('psactuales = '))
c = float(input('ratio pokemon = '))

if a == 0:
    X1=-c/b
else:
X1= (-b+sqrt(b**2-4*a*c))/2*a
X2= (-b-sqrt(b**2-4*a*c))/2*a
print("x1="X1"x2="X2)
