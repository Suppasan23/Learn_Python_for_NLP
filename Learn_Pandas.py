import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# โหลดไฟล์ Excel
df = pd.read_excel("data\Employee.xlsx")

print(df)

df = df.dropna(axis="columns")

print(df)
