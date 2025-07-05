import numpy as np

a = np.array([["a","b","c","d"],
              ["e","f","g","h"],
              ["i","j","k","l"],
              ["m","n","o","p"]])

w = np.hsplit(a,4)


print(w)