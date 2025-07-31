import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# โหลดไฟล์ Excel
df = pd.read_excel("data/Stock.xlsx", index_col="Name")

# ข้อมูลเพิ่มเติม
supplement_product_data = [["แพนด้า", "สัตว์", 5000, 8],
                          ["ฮิปโป", "สัตว์", 8000, 4]]
supplement_product_column = ["Name", "Category", "Price", "Amount"]

# สร้าง DataFrame ใหม่
new_df = pd.DataFrame(data=supplement_product_data, columns=supplement_product_column)
new_df.set_index("Name", inplace=True)

# รวมข้อมูล
df = pd.concat([df, new_df])

print(df)
