import pandas as pd

crypto_data = {
    "Date" : ["2026-01-01", "2026-01-02", "2026-01-03", "2026-01-04", "2026-01-05"],
    "Price" : [35, 25, 23, 56, 43]  

}

df = pd.DataFrame(crypto_data)
df["Date"] = pd.to_datetime(df["Date"])
df.set_index("Date", inplace = True)

rolling_ave = df["Price"].rolling(window = 2).mean()

print(rolling_ave)
print(df)   
