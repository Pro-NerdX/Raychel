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

    def __mul__(self, scalar):
        return Vec3(self.x * scalar, self.y * scalar, self.z * scalar)

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
    
    def norm(self):
        return self / self.length()
    
    def __eq__(self, other):
        if not isinstance(other, Vec3):
            return False
        return self.x == other.x and self.y == other.y and self.z == other.z
