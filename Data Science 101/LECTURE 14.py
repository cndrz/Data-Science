import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

grade_data = {

    "Study_Hours": [2, 5, 8, 10, 12, 15],
    "Grade": [55, 68, 82, 88, 92, 98]
}

df = pd.DataFrame(grade_data)

x = df[["Study_Hours"]] 
y = df["Grade"]

x_train = x.iloc[0:4]
y_train = y.iloc[0:4]
x_test = x.iloc[4:6]
y_test = y.iloc[4:6]

model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R2 Score: {r2}")

