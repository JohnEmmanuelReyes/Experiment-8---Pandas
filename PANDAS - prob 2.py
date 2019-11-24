import pandas as pd

df = pd.read_csv(r'\Users\janjan wangbu\Desktop\cars.csv')

df.iloc[0:5,1:12:2]
df.loc[[0],:]
df.loc[23,'cyl']
df.loc[[1,18,28],['cyl','gear']]
