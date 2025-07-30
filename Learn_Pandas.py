import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve

# สร้างสัญญาณ x และ h
x = np.array([4, 7, 5, 1, 2 ,9,3]) # x คือ สัญญาณอิตพุต
h = np.array([0.0, 1.0, 0.5, 0.2, 0.1, 0.03, 0.01]) # h คือ สัญญาณตอบสนองของระบบ

# คำนวณ Convolution
y = convolve(x, h) # y คือ เอาต์พุตจริง

# สร้างแกนเวลา n สำหรับ y
n = np.arange(len(y))

plt.figure()
plt.stem(n, y, basefmt=" ")
plt.title("Discrete Convolution: y[n] = x[n] * h[n]")
plt.xlabel("n")
plt.ylabel("y[n]")
plt.grid(True)
plt.show()
