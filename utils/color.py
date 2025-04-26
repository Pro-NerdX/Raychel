from utils.interval import Interval
from utils.vec3 import Vec3

Color = Vec3

def write_color(color: Color):
    r = color.x
    g = color.y
    b = color.z

    intensity = Interval(0.000, 0.999)
    rbyte = int(256 * intensity.clamp(r))
    gbyte = int(256 * intensity.clamp(g))
    bbyte = int(256 * intensity.clamp(b))

    return f"{rbyte} {gbyte} {bbyte}\n"
