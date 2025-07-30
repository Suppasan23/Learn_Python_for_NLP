import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# สร้างสัญญาณอินพุตต้นฉบับที่มีทั้งความถี่ต่ำและสูงปนกัน 
# โดยความถี่ต่ำคือเสียงพูดของมนุษย์มีความถี่ 5Hz และ ความถี่สูงคือสัญญาณรบกวนมีความถี่ 50Hz
sampling_frequency = 500  # เก็บค่าสัญญาณจำนวน 500 ตัวอย่างต่อวินาที
time_period = np.linspace(0, 1, sampling_frequency, endpoint=False)  # ช่วงเวลาในการสังเกต 1 วินาที
original_input_signal = np.sin(2*np.pi*5*time_period) + 0.5*np.sin(2*np.pi*50*time_period)  # 5Hz + 50Hz

# แสดงผลกราฟแยก 2 แผง
plt.figure(figsize=(12, 6))

# กราฟ 1 แสดงสัญญาณต้นฉบับ
plt.subplot(2, 1, 1)
plt.plot(time_period, original_input_signal, color='gray')
plt.title('Original Signal (5Hz + 50Hz)')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.grid(True)

# ใช้ฟังก์ชั่น Butterworth filter แบบ btype='low' เพื่อสร้างฟิลเตอร์ในการแยกความถี่ต่ำออกจากความถี่สูง
# ได้ค่า b = numerator coefficients และ a = denominator coefficients ซึ่งเป็นพารามิเตอร์ที่จะนำไปใช้ในการกรองความถี่
cutoff_frequency = 10  # ความถี่ที่ต้องการตัด 10 Hz
transition_band = 4 # ค่าความคมในการตัดความถี่ที่ไม่ต้องการ(ความถี่สูง)ออกไป
b, a = butter(transition_band, cutoff_frequency / (sampling_frequency / 2), btype='low') 

# ใช้ฟิลเตอร์กรองสัญญาณความถี่
filtered_sigal = filtfilt(b, a, original_input_signal)

# กราฟ 2 แสดงสัญญาณที่กรองแล้ว (เหลือแต่ความถี่ต่ำ)
plt.subplot(2, 1, 2)
plt.plot(time_period, filtered_sigal, color='blue')
plt.title('Low-pass: Only ~5Hz remains signal')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()




# แถม ทำการแสดงผลสัญญาณให้เป็นรูปลักษณ์ของ Spectrum โดยใช้ SciPy Fourier Transforms
from scipy.fft import fft, fftfreq

# สร้างแกนความถี่ (1/sampling_frequency)
frequency_axis = fftfreq(sampling_frequency, 1/sampling_frequency)

# ใช้ FFT กับสัญญาณต้นฉบับและสัญญาณที่กรองแล้ว
fft_original = fft(original_input_signal)
fft_filtered = fft(filtered_sigal)

# ตัดเอาเฉพาะครึ่งที่เป็นซีกบวกของ Spectrum
freqs_half = frequency_axis[:sampling_frequency // 2]
magnitude_original = np.abs(fft_original)[:sampling_frequency // 2]
magnitude_filtered = np.abs(fft_filtered)[:sampling_frequency // 2]

# กำหนดขนาดรูปภาพที่จะสร้าง (กว้าง 12 x สูง 6)
plt.figure(figsize=(12, 6))

# กราฟ 3 แสดง Spectrum ของสัญญาณต้นฉบับ
plt.subplot(2, 1, 1)
plt.plot(freqs_half, magnitude_original, color='gray')
plt.title('Frequency Spectrum of Original Signal (5Hz + 50Hz)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.xlim(0, 100)  # แสดง frequency axis แค่ 0 ถึง 100 Hz
plt.grid(True)

# กราฟ 4 แสดง Spectrum ของสัญญาณที่กรองแล้ว (เหลือแต่ความถี่ต่ำ)
plt.subplot(2, 1, 2)
plt.plot(freqs_half, magnitude_filtered, color='blue')
plt.title('Frequency Spectrum of Filtered Signal (Low-pass)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.xlim(0, 100)  # แสดง frequency axis แค่ 0 ถึง 100 Hz
plt.grid(True)
plt.tight_layout()
plt.show()
