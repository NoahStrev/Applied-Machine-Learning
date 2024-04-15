import numpy as np
import pandas as pd
df = pd.read_csv('scalethis.csv')

pd.options.display.max_columns = None
pd.options.display.max_rows = None
dfcols = df.columns
print(df)
print(df.info())

print('\n\nBEFORE STANDARDIZATION')
print(type(df))
print('\nMeans')
print(df.mean(axis=0))
print('\nStandard devs:')
print(df.std(axis=0))

# NOW NORMALIZE THE DATA
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
print(dfcols)
df_scaled = scaler.fit_transform(df)
df_scaled = pd.DataFrame(df_scaled, columns = dfcols)
print(df_scaled)
