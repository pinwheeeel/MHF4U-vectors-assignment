from math import *

class VectorR3:
  def __init__(self, start: list, end: list):
    self.start = start
    self.end = end
    self.x = self.end[0] - self.start[0]
    self.y = self.end[1] - self.start[1]
    self.z = self.end[2] - self.start[2]
    self.mag2 = self.x * self.x + self.y * self.y + self.z * self.z
    self.mag = sqrt(self.mag2)
  
  @property
  def unit(self):
    if self.mag == 0:
      return None
    return self / self.mag
  
  def __str__(self):
    return f"({self.x}, {self.y}, {self.z})"

  def __format__(self, spec):
    formatted = [format(val, spec) for val in [self.x, self.y, self.z]]
    return f"({", ".join(formatted)})"
  
  def __add__(self, other):
    return VectorR3(self.start, [self.end[0] + other.x, self.end[1] + other.y, self.end[2] + other.z])

  def __neg__(self):
    return VectorR3(self.start, [self.start[0] - self.x, self.start[1] - self.y, self.start[2] - self.z])
  
  def __sub__(self, other):
    return self + (-other)

  def __mul__(self, k: int | float):
    return VectorR3(self.start, [self.start[0] + self.x * k, self.start[1] + self.y * k, self.start[2] + self.z * k])
  
  def __rmul__(self, k: int | float):
    return self * k

  def __truediv__(self, k: int | float):
    return self * (1 / k)
  
def dot(u: VectorR3, v: VectorR3):
  return u.x * v.x + u.y * v.y + u.z * v.z

def cross(u: VectorR3, v: VectorR3):
  return VectorR3(u.start, [
    u.start[0] + u.y * v.z - u.z * v.y,
    u.start[1] + u.z * v.x - u.x * v.z,
    u.start[2] + u.x * v.y - u.y * v.x
  ])

def scalar_proj(u: VectorR3, v: VectorR3):
  return dot(u, v) / v.mag

def vector_proj(u: VectorR3, v: VectorR3):
  return dot(u, v) / v.mag2 * v

if __name__ == "__main__":
  exit()