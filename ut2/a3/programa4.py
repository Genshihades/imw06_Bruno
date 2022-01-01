import sys
n=int(sys.argv[1])

if n <= 0:
	print('Por favor, escriba un valor positivo.')
	exit()
else:
	for i in range(1, n + 1):
		result = 1
		for k in range (i, 0, -1):
			result *= k
		print (i,'! =', result)
