import math

from utils.interval import Interval
from utils.vec3 import Vec3

Color = Vec3

def linear_to_gamma(linear_component: float) -> float:
    if (linear_component > 0):
        return math.sqrt(linear_component)
    return 0

def write_color(color: Color):
    r = color.x
    g = color.y
    b = color.z

    # gamma transformation for gamma 2
    r = linear_to_gamma(r)
    g = linear_to_gamma(g)
    b = linear_to_gamma(b)

    intensity = Interval(0.000, 0.999)
    rbyte = int(256 * intensity.clamp(r))
    gbyte = int(256 * intensity.clamp(g))
    bbyte = int(256 * intensity.clamp(b))

    return f"{rbyte} {gbyte} {bbyte}\n"
