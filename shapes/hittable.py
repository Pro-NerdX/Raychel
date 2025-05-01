from typing import List, Optional, TYPE_CHECKING

from utils.interval import Interval
from utils.ray import Ray
from utils.vec3 import Vec3

if TYPE_CHECKING:
    from materials.material import Material # avoid circular imports

class HitRecord:

    def __init__(self, p = Vec3(), normal = Vec3(), t = 0.0, front_face = False):
        self.p = p
        self.normal = normal
        self.material: Optional['Material'] = None
        self.t = t
        self.front_face = front_face
    
    # 
    def set_face_normal(self, ray: Ray, outward_normal: Vec3):
        """
        Sets the hit record normal vector.
        NOTE the parameter `outward_normal` is assumed to have unit length.
        """
        front_face = ray.dir.dot(outward_normal) < 0
        if (front_face):
            self.normal = outward_normal
        else:
            self.normal = outward_normal * -1

class Hittable:
    
    def hit(self, ray: Ray, ray_t: Interval, rec: HitRecord) -> bool:
        raise NotImplementedError
    
class HittableList(Hittable):
    """
    A list of Hittable objects. Implements the Hittable interface itself,
    so a HittableList can be treated as a single Hittable entity.
    """
    def __init__(self, object: Hittable = None):
        self.objects: List[Hittable] = []
        if object:
            self.add(object)

    def clear(self):
        self.objects.clear()
    
    def add(self, object: Hittable):
        self.objects.append(object)
    
    def hit(self, ray: Ray, ray_t: Interval, rec: HitRecord) -> bool:
        temp_rec = HitRecord()
        hit_anything = False
        closest_so_far = ray_t.max_val

        for object in self.objects:
            if object.hit(ray, Interval(ray_t.min_val, closest_so_far), temp_rec):
                hit_anything = True
                closest_so_far = temp_rec.t
                rec.t = temp_rec.t
                rec.p = temp_rec.p
                rec.normal = temp_rec.normal
                # Fix: Not mentioned in the book!
                rec.material = temp_rec.material
        
        return hit_anything
