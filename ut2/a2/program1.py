#programa 1
from math import sqrt
import sys
a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

if a == 0:
    x =-c/b
    print(x)
else:
    X1= (-b+sqrt(b**2-4*a*c))/2*a
    X2= (-b-sqrt(b**2-4*a*c))/2*a
print('x1=',X1,'x2=',X2)
