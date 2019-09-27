class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, objek):
        return Vector(self.a + objek.a, self.b + objek.b)

    def __mul__(self, objek):
        return Vector(self.a * objek.a, self.b * objek.b) 

v1 = Vector(5, 10)
v2 = Vector(4, -2)

print(v1 + v2)
print(v1 + v1)
print(v2 + v2)
print(v1 * v2)
print(v1 * v1)
print(v2 * v2)
