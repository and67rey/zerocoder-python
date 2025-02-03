import pandas as pd

data = pd.read_csv('dz.csv')
df = pd.DataFrame(data)

print(df)
print(df.info())
print(df.describe())

# Удаление записи по Максиму, у которого Salary = NaN
df.drop(7, inplace = True)

print(df)

group = df.groupby('City')['Salary'].mean()
print(group)