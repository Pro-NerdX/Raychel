import math


class Interval:

    empty = None
    universe = None

    def __init__(self, min: float = math.inf, max: float = -math.inf):
        self.min = min
        self.max = max

    def size(self):
        return self.max - self.min
    
    def contains(self, x: float):
        return self.mine <= x <= self.max

    def surrounds(self, x: float):
        return self.min < x < self.max
    
Interval.empty = Interval(math.inf, -math.inf)
Interval.universe = Interval(-math.inf, math.inf)
