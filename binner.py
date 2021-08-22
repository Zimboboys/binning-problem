from point import Point

class Binner:
    def __init__(self, bin_count: int):
        self.bin_count = bin_count

    def bin_point(self, point: Point):
        scalar_names = []
        for s in list(point.get_point()):
            s_scaled = float(s) * float(self.bin_count) # scaling by the amount of bins is a nifty trick
            s_bin = int(s_scaled) # removes trailing comments
            s_name = str(s_bin)
            scalar_names.append(s_name)
        point_name = "".join(scalar_names)
        return point_name