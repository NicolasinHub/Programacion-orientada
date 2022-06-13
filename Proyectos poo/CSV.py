import pandas as pd

miData=pd.read_csv("Predios.csv", nrows=100)

print(miData.head())
print(miData['PRECCONS'])

row=miData.iloc[10]
print(row)

print(miData.shape)