import pandas as pd

delivery_data = {

    "Order_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Minutes": [25, 30, 22, 35, 1500, 28, 32, 5, 29, 31] 
}

df = pd.DataFrame(delivery_data)

Q1 = df["Minutes"].quantile(0.25)
Q3 = df["Minutes"].quantile(0.75)
IQR = Q3 - Q1

lower_fence = (Q1 - 1.5 * IQR)
upper_fence = (Q3 + 1.5 * IQR)

outliers = df[(df["Minutes"] < lower_fence) | (df["Minutes"] > upper_fence)]

print("Deliver Outliers: ")
print(outliers)
