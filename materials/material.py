from abc import ABC, abstractmethod

from shapes.hittable import HitRecord

from utils.color import Color
from utils.ray import Ray
from utils.vec3 import Vec3

# abstract class
class Material:

    @abstractmethod
    def scatter(self, ray_in: Ray, rec: HitRecord) -> tuple[bool, Color, Ray]:
        return False, Color(0, 0, 0), Ray()

class Lambertian(Material):
    def __init__(self, albedo: Color):
        self.albedo = albedo
    
    def scatter(self, ray_in, rec):
        scatter_direction = rec.normal + Vec3.random_norm()

        # catch degenerate scatter direction
        if (scatter_direction.near_zero()):
            scatter_direction = rec.normal

        scattered = Ray(rec.p, scatter_direction)
        attenuation = self.albedo
        return True, attenuation, scattered
