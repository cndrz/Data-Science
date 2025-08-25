import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns = iris.feature_names)
df["target"] = iris.target
df["target_name"] = df["target"].map(lambda i: iris.target_names[i])

print("First 5 rows of the dataset")
print(df.head())

# Basic exploration
print("\n - Dataset Information - \n")

print(df.info())

print("\n - Summary Statistics - \n")
print(df.describe())

print("\n - Class Distribution - \n")
print(df["target_name"].value_counts())

# Visualization
plt.figure(figsize = (8, 6))
plt.scatter(df["sepal length (cm)"], df["sepal width (cm)"], c = df["target"], cmap = "viridis")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.title("Sepal Length vs Width")
plt.show()

# Train-Test Split
X_train, X_test, Y_train, Y_test = train_test_split(iris.data, iris.target, test_size = 0.5, random_state = 50)

# Train Model
model = DecisionTreeClassifier(random_state = 50)
model.fit(X_train, Y_train)

# Make predictions
Y_pred = model.predict(X_test)

# Evaluation
print("\n - Accuracy - \n", accuracy_score(Y_test, Y_pred))
print("\n - Classification Report - \n")
print(classification_report(Y_test, Y_pred, target_names = iris.target_names))

# Visualize Decision Tree
plt.figure(figsize = (12, 8))
plot_tree(model, feature_names = iris.feature_names, class_names = iris.target_names, filled = True)
plt.title("Decision Tree for Iris Classification")
plt.show()