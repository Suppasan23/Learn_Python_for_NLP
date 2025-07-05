import pandas as pd

items = {30:'Mango',10:'Banana',90:'Grape'}

ps_items = pd.Series(items)

print(ps_items)

print(ps_items[10])