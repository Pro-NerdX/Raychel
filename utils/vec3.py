import math
import sys

from utils.random_number_generator import random_float, random_float_range

class Vec3:

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Vec3({self.x}, {self.y}, {self.z})"
    
    def __getitem__(self, index):
        return (self.x, self.y, self.z)[index]

    def __add__(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
        
    def __sub__(self, other):
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, Vec3):
            return Vec3(self.x * other.x, self.y * other.y, self.z * other.z)
        elif isinstance(other, (int, float)):
            return Vec3(self.x * other, self.y * other, self.z * other)
        else:
            print("Vec3.__mul__(): argument was neither int nor float nor Vec3.")
            sys.exit(1)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, scalar):
        return Vec3(self.x / scalar, self.y / scalar, self.z / scalar)
    
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self, other):
        return Vec3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
    
    def length(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
    
    def length_squared(self):
        return self.x ** 2 + self.y ** 2 + self.z ** 2
    
    def near_zero(self) -> bool:
        """ return true, iff vector is close to 0 in all dimensions """
        s = 1e-8
        return self.x < s and self.y < s and self.z < s
    
    def random():
        return Vec3(random_float(), random_float(), random_float())
    
    def random_range(min_val: float, max_val: float):
        return Vec3(random_float_range(min_val, max_val), random_float_range(min_val, max_val), random_float_range(min_val, max_val))

    def norm(self):
        return self / self.length()
    
    def random_norm():
        while True:
            p: Vec3 = Vec3.random_range(-1, 1)
            lensq = p.length_squared()
            if 1e-160 < lensq <= 1: # 1e - 160 == 1 x 10^(-160)
                return p / math.sqrt(lensq)
    
    def random_on_hemisphere(normal):
        if not isinstance(normal, Vec3):
            print("Vec3.random_on_hemisphere: normal was not a Vec3.")
            sys.exit(1)
        
        on_unit_sphere = Vec3.random_norm()
        if (on_unit_sphere.dot(normal) > 0.0):
            return on_unit_sphere
        return on_unit_sphere * -1
    
    def reflect(v, n):
        if not (isinstance(v, Vec3) and isinstance(n, Vec3)):
            print("Vec3.reflect: at least one of the arguments was not a Vec3.")
            sys.exit(1)
        
        return v - n * (2 * v.dot(n))
    
    def __eq__(self, other):
        if not isinstance(other, Vec3):
            return False
        return self.x == other.x and self.y == other.y and self.z == other.z
