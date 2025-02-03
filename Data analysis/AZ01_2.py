import pandas as pd

data = pd.read_csv('dz.csv')
df = pd.DataFrame(data)

print(df)
print()
print(df.info())
print()
print(df.describe())
print()

# Удаление записи по Максиму, у которого Salary = NaN
df.drop(7, inplace = True)
print(df)
print()

group = df.groupby('City')['Salary'].mean()
print(group)