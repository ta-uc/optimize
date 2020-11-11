import numpy as np
import math
def f_1(x):
  # -3*x^6+10x^4-x^3-7x^2
  return -3*math.pow(x,6)+10*math.pow(x,4)-math.pow(x,3)-7*math.pow(x,2)

def d_f_1(x):
  # -18x^5+40x^3-3x^2-14x
  return -18*math.pow(x,5)+40*math.pow(x,3)-3*math.pow(x,2)-14*x

def d_2_f_1(x):
  # -90x^4+120x^2-6x-14
  return -90 * math.pow(x,4)+120*math.pow(x,2)-6*x-14

def f_2(XY):
  x, y = XY
  # -(3x^2+2y^2+3xy)
  return -1*(3*math.pow(x,2)+2*math.pow(y,2)+3*x*y)

def nabra_f_2(XY):
  x, y = XY
  return np.array([-6*x-3*y, -4*y-3*x])

