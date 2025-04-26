from utils.vec3 import Vec3

class Ray:

    def __init__(self, origin=Vec3(0.0, 0.0, 0.0), dir=Vec3(1.0, 0.0, 0.0)):
        self.origin = origin
        self.dir = dir
    
    def at(self, t):
        return self.origin + self.dir * t
