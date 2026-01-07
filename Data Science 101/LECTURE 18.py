import pandas as pd
import kagglehub
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

path = kagglehub.dataset_download("mirichoi0218/insurance")
df = pd.read_csv(f"{path}/insurance.csv")

df_encoded = pd.get_dummies(df, columns = ["smoker"], drop_first = True)
x = df_encoded[["age", "bmi", "children", "smoker_yes"]]
y = df_encoded["charges"]

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

x_train, y_train = x_scaled[:1100], y.iloc[:1100]

model = LinearRegression()
model.fit(x_train, y_train)
print(model.coef_)

