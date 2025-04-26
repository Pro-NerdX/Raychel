import math

from shapes.hittable import HitRecord, Hittable

from utils.ray import Ray
from utils.vec3 import Vec3

class Sphere(Hittable):

    def __init__(self, center: Vec3, radius: float):
        self.center = center
        self.radius = max(0, radius)
    
    def hit(self, ray: Ray, ray_tmin: float, ray_tmax: float, rec: HitRecord) -> bool:
        oc: Vec3 = self.center - ray.origin
        a = ray.dir.length_squared()
        h = ray.dir.dot(oc)
        c = oc.length_squared() - self.radius * self.radius

        discriminant = h * h - a * c
        if discriminant < 0:
            return False
        
        sqrtd = math.sqrt(discriminant)

        root = (h - sqrtd) / a
        if (root <= ray_tmin or ray_tmax <= root):
            root = (h + sqrtd) / a
            if (root <= ray_tmin or ray_tmax <= root):
                return False
            
        rec.t = root
        rec.p = ray.at(rec.t)
        outward_normal = (rec.p - self.center) / self.radius
        rec.set_face_normal(ray, outward_normal)

        return True
