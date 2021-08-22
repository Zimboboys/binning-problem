from point import Point, WeightedPoint
from binner import Binner

# run `python3 sets/generate_sets.py` to generate these files
A_dataset = open("./sets/A.csv", "r")
B_dataset = open("./sets/B.csv", "r")

A_set = []
B_set = []

bin_count = 3
binner = Binner(bin_count)
binned_a = {}

# initialize regions - hardcoded for three dimensions..
region_names = ["{0}{1}{2}".format(i,j,k) for i in range(bin_count) for j in range(bin_count) for k in range(bin_count)]
for region in region_names:
    binned_a[region] = [] 

# extract points from datasets
for a_entry in A_dataset:
    x, y, z, t = a_entry.split(",")
    t = t[:-1] # remove new line

    a_point = Point(float(x), float(y), float(z))
    a = WeightedPoint(a_point, float(t))
    A_set.append(a)

for b_entry in B_dataset:
    x, y, z = b_entry.split(",")
    z = z[:-1] # remove new line

    b = Point(float(x), float(y), float(z))
    B_set.append(b)

# bin points
for a in A_set:
    a_bin = binner.bin_point(a.get_point())
    binned_a[a_bin].append(a)

# find b's group and find closest a in that group
for b in B_set:
    b_bin = binner.bin_point(b)
    a_bar = binned_a[b_bin]

    min_a, min_dist = None, 2
    for a in a_bar:
        distance = b.calc_distance(a.get_point())
        if distance < min_dist:
            min_a, min_dist = a, distance
    
    print(b.get_point(), ":", a.get_weight())