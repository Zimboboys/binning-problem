import random

A = open("./sets/A.csv", "w")
B = open("./sets/B.csv", "w")

A_count = 200
B_count = 3000 # actual problem has this at 300000

# elements of A are of the form (x, y, z, t)
for i in range(A_count):
    x, y, z, t = random.random(), random.random(), random.random(), random.random()
    A.write("{0},{1},{2},{3}\n".format(x, y, z, t))

# elements of B are of the form (x, y, z, t)
for i in range(B_count):
    x, y, z = random.random(), random.random(), random.random()
    B.write("{0},{1},{2}\n".format(x, y, z))

A.close()
B.close()
