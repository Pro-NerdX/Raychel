import math

from shapes.hittable import HitRecord, Hittable

from utils.color import Color, write_color
from utils.interval import Interval
from utils.ray import Ray
from utils.vec3 import Vec3

class Camera:

    def __init__(self, aspect_ratio: float = 1.0, img_width: int = 100):
        self.aspect_ratio = aspect_ratio  # Ratio of image width to height
        self.img_width = img_width    # Width in pixels
        self.img_height = None          # Height will be set during initialization
        self.center = Vec3(0, 0, 0)     # Camera origin

        # These will be initialized in self.initialize()
        self.pixel_00_loc = None
        self.pixel_delta_u = None
        self.pixel_delta_v = None

    def render(self, world: Hittable, filename: str):
        self.initialize()

        # render
        with open(filename, "w") as f:
            f.write("P3\n")
            f.write(f"{self.img_width} {self.img_height}\n")
            f.write("255\n")

            for j in range(0, self.img_height):
                print(f"\rScanlines remaining: {self.img_height - j}")
                for i in range(0, self.img_width):
                    pixel_center = self.pixel_00_loc + (self.pixel_delta_u * i) + (self.pixel_delta_v * j)
                    ray_direction = pixel_center - self.center
                    ray = Ray(self.center, ray_direction)
                
                    pixel_color = self.ray_color(ray, world)
                    f.write(f"{write_color(pixel_color)}")
        print("\rDone.\n")
    
    def initialize(self):
        self.img_height = max(1, int(self.img_width / self.aspect_ratio))

        # camera
        focal_length = 1.0
        viewport_height = 2.0
        viewport_width = viewport_height * (float(self.img_width) / self.img_height)
        camera_center = Vec3(0, 0, 0)

        # viewport calculations
        viewport_u = Vec3(viewport_width, 0, 0)
        viewport_v = Vec3(0, -viewport_height, 0)

        # horizontal and vertical delta vectors from pixel to pixel
        self.pixel_delta_u = viewport_u / self.img_width
        self.pixel_delta_v = viewport_v / self.img_height

        # upper left pixel
        viewport_upper_left = camera_center - Vec3(
            0, 0, focal_length
        ) - viewport_u / 2 - viewport_v / 2
        self.pixel_00_loc = viewport_upper_left + (self.pixel_delta_u + self.pixel_delta_v) * 0.5
    
    def ray_color(self, ray: Ray, world: Hittable):
        rec = HitRecord()
        if (world.hit(ray, Interval(0, math.inf), rec)):
            return (rec.normal + Color(1, 1, 1)) * 0.5
        
        unit_direction = ray.dir.norm()
        a = 0.5 * (unit_direction.y + 1.0)
        return Color(1.0, 1.0, 1.0) * (1.0 - a) + Color(0.5, 0.7, 1.0) * a
