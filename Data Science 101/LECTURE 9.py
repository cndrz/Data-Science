import pandas as pd

retail_data = {
    "City": ["Manila", "Manila", "Cebu", "Cebu", "Davao", "Davao", "Manila", "Cebu"],
    "Product": ["Laptop", "Phone", "Laptop", "Phone", "Laptop", "Phone", "Laptop", "Tablet"],
    "Sales": [50000, 20000, 45000, 25000, 30000, 15000, 52000, 10000]
}

df = pd.DataFrame(retail_data)

pivot = df.pivot_table(index = "City", columns = "Product", values = "Sales", aggfunc = "sum")
pivot = pivot.fillna(0)

print("Summary Pivot Table: ")
print(pivot)