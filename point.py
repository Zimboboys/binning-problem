class Point:
    def __init__(self, x: float, y: float, z: float):
        self.point = (x, y, z)

    def get_point(self):
        return self.point

    # calculates Euclidean distance
    def calc_distance(self, point_2):
        distance = 0
        dimensions = len(self.point)
        for i in range(dimensions):
            diff = point_2.point[i] - self.point[i]
            distance = diff ** 2
        return distance ** 0.5
    
    def __str__(self):
        return "({0}, {1}, {2})".format(self.point[0], self.point[1], self.point[2])

class WeightedPoint:
    def __init__(self, point: Point, weight: float):
        self.point = point
        self.weight = weight
    
    def get_point(self) -> Point:
        return self.point
    
    def get_weight(self):
        return self.weight
