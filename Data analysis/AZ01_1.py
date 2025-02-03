import pandas as pd

data = pd.read_csv('Kepler Telescope Exoplanets.csv')
df = pd.DataFrame(data)

print(df.head())

print(df.info())

print(df.describe())

