import pandas as pd
import numpy as np

raw_data = {
    "Customer_Name" : ["JM", "Ally", "Anastacia", None],
    "Spend" : [234, 125, np.nan, np.nan],
    "Rating" : [5, 2, 1, np.nan]
}

df = pd.DataFrame(raw_data)

print(df.isnull().sum())

df = df.drop_duplicates()
df["Rating"] = df["Rating"].fillna(df["Rating"].mean())
df = df.dropna(subset = ["Customer_Name"])

print("Cleaned DataFrame: ")
print(df)