import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# โหลดไฟล์ Excel
df = pd.read_excel("data/Stock.xlsx",index_col="Name")

df["total"] = df["Price"]*df["Amount"]

print(df.sum())
