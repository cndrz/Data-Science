import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay
import kagglehub

path = kagglehub.dataset_download("yasserh/wine-quality-dataset")
df = pd.read_csv(f"{path}/WineQT.csv")

print(df.head())
print(df.info())
print(df["quality"].value_counts())

df["good_wine"] = (df["quality"] >= 7).astype(int)

x = df.drop(["quality", "good_wine", "Id"], axis = 1)
y = df["good_wine"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

tree_model = DecisionTreeClassifier(random_state = 42)
tree_model.fit(x_train, y_train)

y_pred = tree_model.predict(x_test)

print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print(f"\nClassification Report: ")
print(classification_report(y_test, y_pred))

ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
plt.title("Decision Tree: Wine Quality Prediction")
plt.show()