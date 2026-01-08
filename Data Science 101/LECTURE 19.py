import pandas as pd
import kagglehub
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

path = kagglehub.dataset_download("mirichoi0218/insurance")
df = pd.read_csv(f"{path}/insurance.csv")

df_encoded = pd.get_dummies(df, columns = ["smoker"], drop_first = True)
x = df_encoded[["age", "bmi", "children", "smoker_yes"]]
y = df_encoded["charges"]

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size = 0.2, random_state = 42)

model = LinearRegression()
model.fit(x_train, y_train)
print(model.score(x_test, y_test))

