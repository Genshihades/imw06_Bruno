import sys
Eu = int(sys.argv[1])
n1 = Eu // 50
if n1>0:
   print(n1, "billetes de 50 bolivares")
Eu2=Eu-(n1*50)
n3=Eu2 // 20
if n3>0:
  print(n3, "billetes de 20 bolivares")
Eu3=Eu2-(n3*20)
n4=Eu3 // 10
if n4>0:
   print(n4, "billetes de 10 chelines")
Eu4=Eu3-(n4*10)
n5= Eu4 // 5
if n5>0:
   print(n5, "Billetes de 5 chelines")
Eu5 = Eu4-(n5*5)
n6= Eu5 // 2
if n6>0:
   print(n6, "monedita de 2 chelines")
Eu6 = Eu5-(n6*2)
n7= Eu6 // 1
if n7>0:
   print(n7, "monedita de 1 chelin")
if Eu == 0:
   print("no hay dinero")
