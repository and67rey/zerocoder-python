import pandas as pd

df = pd.read_csv('dz.csv')

print(df)
print()
print(df.info())
print()
print(df.describe())
print()

group = df.groupby('City')['Salary'].mean()
print(group)