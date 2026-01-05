import pandas as pd

grade_data = {

    "Study_Hours": [2, 5, 8, 10, 12, 15],
    "Grade": [55, 68, 82, 88, 92, 98]
}

df = pd.DataFrame(grade_data)

x = df["Study_Hours"]
y = df["Grade"]

x_train = x.iloc[0 : 4]
y_train = y.iloc[0 : 4]

x_test = x.iloc[4 : 6]
y_test = y.iloc[4 : 6]

print(x_test)
print(x_train)