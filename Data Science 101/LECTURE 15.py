import pandas as pd
import kagglehub
from sklearn.linear_model import LinearRegression

path = kagglehub.dataset_download("mirichoi0218/insurance")
print("Path to dataset files:", path)

df = pd.read_csv(f"{path}/insurance.csv")
x = df[["age", "bmi", "children"]]
y = df["charges"]

x_train = x.iloc[:1001]
y_train = y.iloc[:1001]

x_test = x.iloc[1001:]
y_test = y.iloc[1001:]

model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print(y_pred)