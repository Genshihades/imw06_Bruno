import sys
from math import sqrt
x1 = int(sys.argv[1])
y1 = int(sys.argv[2])
x2 = int(sys.argv[3])
y2 = int(sys.argv[4])
x3 = int(sys.argv[5])
y3 = int(sys.argv[6])
p = (sqrt((x1-x2)**2+(y1-y2)**2))
h = (sqrt((x1-x3)**2+(y1-y3)**2))
print (p, h)
if p < h:
        print("El punto más cercano a",(x1,y1), "es",(x2,y2), "y está a una distancia de ",p)
else:
        print("El punto más cercano a",(x1,y1), "es",(x3,y3), "y está a una distancia de ",h)
