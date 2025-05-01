from materials.material import Material

from utils.color import Color
from utils.ray import Ray
from utils.vec3 import Vec3

class Metal(Material):
    def __init__(self, albedo: Color):
        self.albedo = albedo

    def scatter(self, ray_in, rec):
        reflected: Vec3 = Vec3.reflect(ray_in.dir, rec.normal)
        scattered = Ray(rec.p, reflected)
        attenuation = self.albedo
        return True, attenuation, scattered
