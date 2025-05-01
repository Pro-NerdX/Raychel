import sys

from materials.material import Lambertian
from materials.metal import Metal

from shapes.hittable import HittableList
from shapes.sphere import Sphere

from utils.camera import Camera
from utils.color import Color
from utils.vec3 import Vec3

def main():
    # command line args
    if not len(sys.argv) <= 2:
        print("Usage: see README.md")
        sys.exit(1)
    filename = "img.ppm"
    if len(sys.argv) > 1:
        filename = f"{sys.argv[1]}.ppm"
    
    # world
    world = HittableList()

    material_ground = Lambertian(Color(0.8, 0.8, 0.0))
    material_center = Lambertian(Color(0.1, 0.2, 0.5))
    material_left = Metal(Color(0.8, 0.8, 0.8), 0.3)
    material_right = Metal(Color(0.8, 0.6, 0.2), 1.0)

    world.add(Sphere(Vec3(0.0, -100.5, -1.0), 100.0, material_ground))
    world.add(Sphere(Vec3(0.0, 0.0, -1.2), 0.5, material_center))
    world.add(Sphere(Vec3(-1.0, 0.0, -1.0), 0.5, material_left))
    world.add(Sphere(Vec3(1.0, 0.0, -1.0), 0.5, material_right))

    # cam
    cam = Camera()
    cam.aspect_ratio        = 16.0 / 9.0
    cam.img_width           = 400
    cam.samples_per_pixel   = 100
    cam.max_depth           = 50
    
    # render
    cam.render(world, filename)

if __name__ == "__main__":
    main()
