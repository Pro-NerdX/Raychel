import math
import sys

from shapes.hittable import HitRecord, Hittable, HittableList
from shapes.sphere import Sphere

from utils.ray import Ray
from utils.vec3 import Vec3
from utils.color import Color, write_color

def ray_color(ray: Ray, world: Hittable):
    rec = HitRecord()
    if (world.hit(ray, 0, float('inf'), rec)):
        return (rec.normal + Color(1, 1, 1)) * 0.5
        
    unit_direction = ray.dir.norm()
    a = 0.5 * (unit_direction.y + 1.0)
    return Color(1.0, 1.0, 1.0) * (1.0 - a) + Color(0.5, 0.7, 1.0) * a

def main():
    # command line args
    if not len(sys.argv) <= 2:
        print("Usage: see README.md")
        sys.exit(1)
    filename = "img.ppm"
    if len(sys.argv) > 1:
        filename = f"{sys.argv[1]}.ppm"

    # img
    aspect_ratio = 16.0 / 9.0
    img_width = 400
    
    img_height = int(img_width / aspect_ratio)
    if img_height < 1:
        img_height = 1
    
    # world
    world = HittableList()

    world.add(Sphere(Vec3(0, 0, -1), 0.5))
    world.add(Sphere(Vec3(0, -100.5, -1), 100))

    # camera
    focal_length = 1.0
    viewport_height = 2.0
    viewport_width = viewport_height * (float(img_width) / img_height)
    camera_center = Vec3(0, 0, 0)

    # viewport calculations
    viewport_u = Vec3(viewport_width, 0, 0)
    viewport_v = Vec3(0, -viewport_height, 0)

    # horizontal and vertical delta vectors from pixel to pixel
    pixel_delta_u = viewport_u / img_width
    pixel_delta_v = viewport_v / img_height

    # upper left pixel
    viewport_upper_left = camera_center - Vec3(
        0, 0, focal_length
    ) - viewport_u / 2 - viewport_v / 2
    pixel_00_loc = viewport_upper_left + (pixel_delta_u + pixel_delta_v) * 0.5

    # render
    with open(filename, "w") as f:
        f.write("P3\n")
        f.write(f"{img_width} {img_height}\n")
        f.write("255\n")

        for j in range(0, img_height):
            print(f"\rScanlines remaining: {img_height - j}")
            for i in range(0, img_width):
                pixel_center = pixel_00_loc + (pixel_delta_u * i) + (pixel_delta_v * j)
                ray_direction = pixel_center - camera_center
                ray = Ray(camera_center, ray_direction)
                
                pixel_color = ray_color(ray, world)
                f.write(f"{write_color(pixel_color)}")
    
    print("\rDone.\n")

if __name__ == "__main__":
    main()
