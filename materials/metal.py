from materials.material import Material

from utils.color import Color
from utils.ray import Ray
from utils.vec3 import Vec3

class Metal(Material):
    def __init__(self, albedo: Color, fuzz: float):
        self.albedo = albedo
        self.fuzz = fuzz

    def scatter(self, ray_in, rec):
        reflected: Vec3 = Vec3.reflect(ray_in.dir, rec.normal)
        reflected = reflected.norm() + (self.fuzz * Vec3.random_norm())
        scattered = Ray(rec.p, reflected)
        attenuation = self.albedo
        return scattered.dir.dot(rec.normal), attenuation, scattered
