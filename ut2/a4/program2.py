import random

NUCLEOBASES = "ATGC"
DNA_SIZE = 100

sequence = ''.join([random.choice(NUCLEOBASES) for i in range(DNA_SIZE)])

