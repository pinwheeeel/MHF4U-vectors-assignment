from vectors import *
from math import *
import sympy as sp

def main():
  number = input("Enter student number: ")
  number = number[:9].zfill(9)

  br(0)
  print(f"Student number: {number}")

  br(1)
  a = [ int(number[0]), -int(number[1]),  int(number[2])]
  b = [-int(number[3]),  int(number[4]), -int(number[5])]
  c = [ int(number[6]), -int(number[7]),  int(number[8])]

  print(f"A{a}")
  print(f"B{b}")
  print(f"C{c}")

  br(2)
  ab = VectorR3(a, b)
  bc = VectorR3(b, c)
  ca = VectorR3(c, a)
  ba = -ab
  cb = -bc
  ac = -ca

  oa = VectorR3([0, 0, 0], a)
  ob = VectorR3([0, 0, 0], b)
  oc = VectorR3([0, 0, 0], c)
  ao = -oa
  bo = -ob
  co = -oc

  print(f"AB{ab}")
  print()
  print(f"BC{bc}")
  print(f"AC{ac}")

  br(3)
  print(f"Perimeter = |AB| + |BC| + |CA|")
  print(f"Perimeter = sqrt({ab.mag2}) + sqrt({bc.mag2}) + sqrt({ca.mag2}) = {ab.mag + bc.mag + ca.mag :.3f}")
  
  br(4)
  print(f"AB{ab}, AC{ac}")
  theta = acos(dot(ab, ac) / (ab.mag * ac.mag))
  print(f"\u03b8 = arccos(AB \u22c5 AC / (|AB| * |AC|)")
  print(f"\u03b8 = arccos({dot(ab, ac)} / [ sqrt({ab.mag2 * ac.mag2}) ] )")
  print(f"\u03b8 = {degrees(theta):.3f}\u00b0")

  br(5)
  abxac = cross(ab, ac)
  print(f"[ABC] = 1/2 * |AB \u2a2f AC|")
  print(f"      = 1/2 * |{abxac}|")
  print(f"      = sqrt({abxac.mag2})/2")
  print(f"[ABC] = {sp.simplify(sp.sqrt(abxac.mag2) / 2)} = {abxac.mag / 2 :.3f}")

  br(6)
  pp_volume = abs(dot(oa, cross(ob, oc)))
  print(f"Volume = 1/6 * |OA \u22c5 (OB \u2a2f OC)|")
  print(f"       = 1/6 * |{oa} \u22c5 ({ob} \u2a2f {oc})|")
  print(f"       = 1/6 * |{oa} \u22c5 {cross(ob, oc)}|")
  print(f"Volume = {pp_volume}/6 = {sp.Rational(pp_volume, 6)} = {pp_volume/6 :.3f}")

  br(7)
  median = ab + bc/2
  print(f"u = AM/|AM| = (AB + BC/2)/|AB + BC/2|")
  print(f"AB + BC/2 = {ab} + {bc/2} = {ab + bc/2}")
  print(f"|AB + BC/2| = sqrt({(2*ab + bc).mag2})/2 = {median.mag :.3f}")
  print(f"u = 2/sqrt({(2*ab + bc).mag2}) * {median} = 1/sqrt({(2*ab + bc).mag2}) * {2*ab + bc} = {median.unit :.4f}")

  br(8)
  dist = abs(scalar_proj(oa, cross(ab, bc)))
  print(f"d = |OA \u22c5 (AB \u2a2f BC)| / |AB \u2a2f BC|")
  print(f"  = | {oa} \u22c5 ({ab} \u2a2f {bc}) | / |{cross(ab, bc)}|")
  print(f"  = | {oa} \u22c5 {cross(ab, bc)} | / sqrt({cross(ab, bc).mag2})")
  print(f"d = {abs(dot(oa, cross(ab, bc)))}/sqrt({cross(ab, bc).mag2}) = {dist :.3f}")

  br(9)
  """
  Let AH be the altitude of the triangle where H is on line BC
  AH = AB + BH
     = AB + vector_proj(BA, BC)
  then find unit vector of AH
  u = AH/|AH|
  """
  ah = ab + vector_proj(ba, bc)
  print(f"AH = AB + BH")
  print(f"   = AB + vector_proj(BA onto BC)")
  print(f"   = AB + (BA \u22c5 BC)/|BC|^2 * BC")
  print(f"   = {ab} + ({ba} \u22c5 {bc})/|{bc}|^2 * {bc}")
  print(f"   = {ab} + {dot(ba, bc)}/{bc.mag2} * {bc}")
  print(f"   = 1/{bc.mag2} * {ab*bc.mag2 + bc*dot(ba, bc)}")
  print(f"   = {ah :.4f}")
  ah_bcmag2 = ab*bc.mag2 + bc*dot(ba, bc)
  print(f"u = AH/|AH| = 1/sqrt({ah_bcmag2.mag2}) * {ah_bcmag2}")
  print(f"  = {ah.unit :.4f}")
  
  br(10)
  """
  same as 9
  """

  print(f"Same as 9")
  v = cross(bc, cross(bc, ba))
  print(f"v = BC \u2a2f (BC \u2a2f BA)")
  print(f"  = {bc} \u2a2f ({bc} \u2a2f {ba})")
  print(f"  = {bc} \u2a2f {cross(bc, ba)}")
  print(f"  = {cross(bc, cross(bc, ba))}")
  print(f"v = {v :}")
  print(f"u = v/|v|")
  print(f"  = 1/sqrt({v.mag2}) * {v}")
  print(f"  = {v.unit :.4f}")

  br(11)
  """
  let u = AB/|AB|, v = AC/|AC|
  w = (u+v)/|u+v| which is an angle bisector unit vector of A
  w = (AB/|AB| + AC/|AC|)/|AB/|AB| + AC/|AC||
  """

  print(f"u = AB/|AB| = {ab}/sqrt({ab.mag2}) = {ab.unit :.4f}")
  print(f"v = AC/|AC| = {ac}/sqrt({ac.mag2}) = {ac.unit :.4f}")
  u = ab.unit
  v = ac.unit
  w = u+v
  print(f"w = (u+v)/|u+v| = ({u:.4f} + {v:.4f})/|{u:.4f} + {v:.4f}|")
  print(f"  = 1/{w.mag:.4f} * {w:.4f}")
  print(f"  = {1/w.mag:.4f} * {w:.4f}")
  print(f"w_unit = {w.unit :.4f}")

  print()
  print(f"Method 2")

  w = ab * ac.mag + ac * ab.mag
  print(f"w = AB * |AC| + AC * |AB|")
  print(f"w = sqrt({ac.mag2}) * {ab} + sqrt({ab.mag2}) * {ac}")
  print(f"  = {w :.4f}")
  print(f"w_unit = {w.unit :.4f}")

  br(00)


def br(num):
  print()
  print("="*14 + f" {num:02} " + "="*14)
  print()

main()