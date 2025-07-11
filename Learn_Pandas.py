import pandas as pd

cols = [0,2]

df_Zoo = pd.read_csv("Zoo.csv", encoding="utf-8", usecols=cols)

print(df_Zoo)
