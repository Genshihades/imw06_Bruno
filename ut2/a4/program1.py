import sys

dni=int(sys.argv[1])

palabra='TRWAGMYFPDXBNJZSQVHLCKE'

print ("El DNI completo es",dni,palabra[dni%23])
