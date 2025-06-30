import numpy as np

a = np.array([[5,1,7],
              [9,3,4],
              [8,2,7]])

b = np.array([[10,20,30],
              [40,50,90],
              [80,100,5]])
 
t = a.dot(b)

print(t)