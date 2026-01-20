import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay
import kagglehub

path = kagglehub.dataset_download("johnsmith88/heart-disease-dataset")
df = pd.read_csv(f"{path}/heart.csv")

print(df.head())
print(df.info())
print(df["target"].value_counts())

x = df.drop("target", axis = 1)
y = df["target"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

tree_model = DecisionTreeClassifier(random_state = 42)
tree_model.fit(x_train, y_train)
tree_pred = tree_model.predict(x_test)

print("=" * 50)
print("Single Decision Tree Results:")
print(f"Accuracy: {accuracy_score(y_test, tree_pred):.2f}")
print(classification_report(y_test, tree_pred))

forest_model = RandomForestClassifier(n_estimators = 100, random_state = 42)
forest_model.fit(x_train, y_train)
forest_pred = forest_model.predict(x_test)

print("=" * 50)
print("Random Forest Results (100 Trees):")
print(f"Accuracy: {accuracy_score(y_test, forest_pred):.2f}")
print(classification_report(y_test, forest_pred))

fig, axes = plt.subplots(1, 2, figsize = (12, 5))

ConfusionMatrixDisplay.from_predictions(y_test, tree_pred, ax=axes[0])
axes[0].set_title(f"Decision Tree\nAccuracy: {accuracy_score(y_test, tree_pred):.2f}")

ConfusionMatrixDisplay.from_predictions(y_test, forest_pred, ax=axes[1])
axes[1].set_title(f"Random Forest (100 trees)\nAccuracy: {accuracy_score(y_test, forest_pred):.2f}")

plt.tight_layout()
plt.show()