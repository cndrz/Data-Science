import pandas as pd
import matplotlib.pyplot as plt

house_data = {
    "SqFt" : [12, 23, 52, 24, 54],
    "Price" : [24233, 23252, 1235, 12356, 13562]
}

df = pd.DataFrame(house_data)

plt.scatter(df["SqFt"], df["Price"], color = "red", marker = "X")
plt.title("House Size to Price Relation")
plt.xlabel("Square Feet")
plt.ylabel("Price")
plt.grid(True)
plt.show()