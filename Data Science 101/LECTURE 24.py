import pandas as pd
import kagglehub
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

path = kagglehub.dataset_download("mirichoi0218/insurance")
df = pd.read_csv(f"{path}/insurance.csv")

df["smoker"] = df["smoker"].map({"yes" : 1, "no" : 0})
x = df[["age", "bmi", "children"]]
y = df["smoker"]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.8, random_state = 42)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)

x_test_scaled = scaler.transform(x_test)

model = KNeighborsClassifier(n_neighbors = 5)
model.fit(x_train_scaled, y_train)
y_pred = model.predict(x_test_scaled)

cm = confusion_matrix(y_test, y_pred)
ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
print(classification_report(y_test, y_pred))
plt.show()


x_test_scaled = scaler.fit_transform(x_test)

model = KNeighborsClassifier(n_neighbors = 5)
model.fit(x_train_scaled, y_train)
y_pred = model.predict(x_test_scaled)
