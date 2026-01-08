import pandas as pd
import kagglehub
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

path = kagglehub.dataset_download("mirichoi0218/insurance")
df = pd.read_csv(f"{path}/insurance.csv")

df["smoker"] = df["smoker"].map({"yes" : 1, "no" : 0})
x = df[["age", "bmi", "charges"]]
y = df["smoker"]

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, train_size = 0.8, random_state = 42)

model = LogisticRegression()
model.fit(x_train, y_train)
print(model.score(x_test, y_test))
