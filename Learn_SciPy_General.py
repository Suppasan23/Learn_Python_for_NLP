import numpy as np
from scipy.spatial import ConvexHull
from scipy.integrate import quad, nquad, dblquad, tplquad
from scipy.optimize import root
import matplotlib.pyplot as plt

def func(x):
  return x + np.sin(x)
input = 0.1
result = root(func, input)

print(result)
