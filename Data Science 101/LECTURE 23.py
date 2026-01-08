import pandas as pd
import kagglehub
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

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

y_pred = model.predict(x_test)

cm = confusion_matrix(y_test, y_pred)
ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
print(classification_report(y_test, y_pred))
plt.show()
