import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve

# สร้างสัญญาณ x และ h
x = np.array([4, 7, 5, 1, 2 ,9,3]) # x คือ สัญญาณอิตพุต
h = np.array([2, 1.0, 0.5, 0.2, 0.1, 0.03, 0.01]) # h คือ สัญญาณของระบบ

# คำนวณ Convolution
y = convolve(x, h) # y คือ สัญญาณเอาต์พุตจริง

# สร้างแกนเวลา
n_x = np.arange(len(x))
n_h = np.arange(len(h))
n_y = np.arange(len(y))

# กำหนดขนาดรูปภาพที่จะสร้าง (กว้าง 12 x สูง 8)
plt.figure(figsize=(12,8))

# แสดง x[n]
plt.subplot(3,1,1)
plt.stem(n_x, x, basefmt=" ")
plt.title("Input Signal: x[n]")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.grid(True)

# แสดง h[n]
plt.subplot(3,1,2)
plt.stem(n_h, h, basefmt=" ")
plt.title("System Response: h[n]")
plt.xlabel("n")
plt.ylabel("h[n]")
plt.grid(True)

# แสดง y[n] = x[n] * h[n]
plt.subplot(3,1,3)
plt.stem(n_y, y, basefmt=" ")
plt.title("Output Signal: y[n] = x[n] * h[n]")
plt.xlabel("n")
plt.ylabel("h[n]")
plt.grid(True)

plt.tight_layout()
plt.show()