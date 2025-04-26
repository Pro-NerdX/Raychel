import random

def random_float() -> float:
    """ returns a random float number x with 0 <= x < 1 """
    return random.uniform(0.0, 1.0)

def random_float_range(min_val, max_val) -> float:
    """ returns a random real in [0, 1) """
    return min_val + (max_val - min_val) * random_float()
