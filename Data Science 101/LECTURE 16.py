import pandas as pd
import kagglehub
from sklearn.linear_model import LinearRegression

path = kagglehub.dataset_download("mirichoi0218/insurance")
df = pd.read_csv(f"{path}/insurance.csv")
x = df[["age", "bmi", "children"]]
y = df["charges"]
x_train, y_train = x.iloc[:1000], y.iloc[:1000]

model = LinearRegression()
model.fit(x_train, y_train)

coefficient = model.coef_
intercept = model.intercept_

print(f"Model Coefficient: {coefficient}")
print(f"Model Intercept: {intercept}")