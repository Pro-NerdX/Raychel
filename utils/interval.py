import math


class Interval:

    empty = None
    universe = None

    def __init__(self, min_val: float = math.inf, max_val: float = -math.inf):
        self.min_val = min_val
        self.max_val = max_val

    def size(self):
        return self.max_val - self.min_val
    
    def contains(self, x: float):
        return self.min_val <= x <= self.max_val

    def surrounds(self, x: float):
        return self.min_val < x < self.max_val
    
    def clamp(self, x: float):
        if x < self.min_val:
            return self.min_val
        elif x > self.max_val:
            return self.max_val
        return x
    
Interval.empty = Interval(math.inf, -math.inf)
Interval.universe = Interval(-math.inf, math.inf)
