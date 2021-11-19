import sys
a = float(sys.argv[1])

if a < 5:
    print('suspenso')
elif a >= 5 and a < 7:
        print("aprobado")
elif a >= 7 and a <= 8:
        print("notable")
elif a >=9 and a < 10:
    print("sobresaliente")
elif a == 10:
        print("Matricula de honor")