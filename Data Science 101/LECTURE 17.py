import pandas as pd
import kagglehub
from sklearn.linear_model import LinearRegression

path = kagglehub.dataset_download("mirichoi0218/insurance")
df = pd.read_csv(f"{path}/insurance.csv")

print(df.head)

df_encoded = pd.get_dummies(df, columns = ["smoker"], drop_first = True)
x = df_encoded[["age", "bmi", "children", "smoker_yes"]]
y = df_encoded["charges"]

x_train, y_train = x.iloc[:1100], y.iloc[:1100]

model = LinearRegression()
model.fit(x_train, y_train)

coefficient = model.coef_
print("Coefficients for [age, bmi, children, smoker_yes]: ")
print(coefficient)
