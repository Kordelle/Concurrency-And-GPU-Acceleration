# Performance benchmarking for Pandas operations on CPU

import pandas as pd
import time

start_time = time.time()

df = pd.read_csv('large_dataset.csv')
df.groupby('column_name').agg({'value_column': 'sum'})
#Aditional Operations

end_time = time.time()

print(f"CPU Runtime: {end_time - start_time} seconds")

