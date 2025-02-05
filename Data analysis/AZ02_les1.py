import pandas as pd

import numpy as np

dates = pd.date_range(start='2022-07-26', periods=60, freq='D')

values = np.random.rand(60)

df = pd.DataFrame({'Date': dates, 'Value': values})

df.set_index('Date', inplace=True)

month = df.resample('M').mean()

print(df)
print(month)

