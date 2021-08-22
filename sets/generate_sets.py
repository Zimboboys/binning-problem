import random, os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from point import Point, WeightedPoint

A = open("./sets/A.csv", "w")
B = open("./sets/B.csv", "w")
expected = open("./sets/expected.out", "w")

A_count = 100 # actual problem has this at 300
B_count = 20000 # actual problem has this at 300000

A_set = []
B_set = []

for i in range(A_count):
    x, y, z, t = random.random(), random.random(), random.random(), random.random()
    A.write("{},{},{},{}\n".format(x, y, z, t))
    a_point = Point(x, y, z)
    a = WeightedPoint(a_point, t)
    A_set.append(a)

# elements of B are Points
for i in range(B_count):
    x, y, z = random.random(), random.random(), random.random()
    B.write("{},{},{}\n".format(x, y, z))
    b = Point(x, y, z)
    B_set.append(b)

# generate expected pairings
for b in B_set:
    min_a, min_dist = None, 2
    for a in A_set:
        distance = b.calc_distance(a.get_point())
        if distance < min_dist:
            min_a, min_dist = a, distance
    
    expected.write("{},{},{},{}\n".format(b.get_point()[0], b.get_point()[1], b.get_point()[2], min_a.get_weight()))

A.close()
B.close()
expected.close()
