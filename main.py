import sys

from shapes.hittable import HittableList
from shapes.sphere import Sphere

from utils.camera import Camera
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

    world.add(Sphere(Vec3(0, 0, -1), 0.5))
    world.add(Sphere(Vec3(0, -100.5, -1), 100))

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
