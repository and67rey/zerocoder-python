import pandas as pd

df = pd.read_csv('Kepler Telescope Exoplanets.csv')

print(df.head())
print()
print(df.info())
print()
print(df.describe())

