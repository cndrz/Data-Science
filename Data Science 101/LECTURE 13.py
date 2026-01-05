import pandas as pd 
from sklearn.linear_model import LinearRegression

grade_data = {

    "Study_Hours": [2, 5, 8, 10, 12, 15],
    "Grade": [55, 68, 82, 88, 92, 98]
}

df = pd.DataFrame(grade_data)

x_train = df["Study_Hours"].iloc[0:3]
y_train = df["Grade"].iloc[0:3]

x_test = df["Study_Hours"].iloc[4:6]

model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print(f"Model Coefficient: {model.coef_}")
print(f"Model Intercept: {model.intercept_}")

