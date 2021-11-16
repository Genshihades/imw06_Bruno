import sys
Eu = int(sys.argv[1])
n1 = Eu // 50
print(n1, "billetes de 50")
Eu2=Eu-(n1*50)
n3=Eu2 // 20
print(n3, "billetes de 20")
Eu3=Eu2-(n3*20)
n4=Eu3 // 10
print(n4, "billetes de 10")
Eu4=Eu3-(n4*10)
n5= Eu4 // 5
print(n5, "Billetes de 5")
Eu5 = Eu4-(n5*5)
n6= Eu5 // 2
print(n6, "moneditas de 2")
Eu6 = Eu5-(n6*2)
n7= Eu6 // 1
print(n7, "moneditas de 1")
