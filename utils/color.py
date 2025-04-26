from utils.vec3 import Vec3

Color = Vec3

def write_color(color: Color):
    r = color.x
    g = color.y
    b = color.z

    rbyte = int(255.999 * r)
    gbyte = int(255.999 * g)
    bbyte = int(255.999 * b)

    return f"{rbyte} {gbyte} {bbyte}\n"
