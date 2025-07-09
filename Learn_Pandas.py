import pandas as pd

name = ["คีย์บอร์ด","เมาส์","ตุ๊กตา"]
category = ["อุปกรณ์คอม","อุปกรณ์คอม","ของเล่น"]
price = [500,300,900]

s_name = pd.Series(name)
s_category = pd.Series(category)
s_price = pd.Series(price)

frame = {"ชื่อสินค้า":s_name,"หมวดหมู่":s_category,"ราคา":s_price}

df = pd.DataFrame(frame)

print(df)

df.to_csv("pandas_products.csv")
