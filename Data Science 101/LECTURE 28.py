import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay

cancer = load_breast_cancer()
x = cancer.data
y = cancer.target

print(f"Dataset Shape: {x.shape}")
print(f"Features: {cancer.feature_names[:5]}...")
print(f"Classes: {cancer.target_names}")

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.2, random_state = 42)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

print("\n" + "=" * 60)

tree_model = DecisionTreeClassifier(random_state = 42)
tree_model.fit(x_train_scaled, y_train)
tree_pred = tree_model.predict(x_test_scaled)
tree_acc = accuracy_score(y_test, tree_pred)
print(f"Decision Tree Accuracy: {tree_acc:.3f}")

forest_model = RandomForestClassifier(n_estimators = 100, random_state = 42)
forest_model.fit(x_train_scaled, y_train)
forest_pred = forest_model.predict(x_test_scaled)
forest_acc = accuracy_score(y_test, forest_pred)
print(f"Random Forest Accuracy: {forest_acc:.3f}")

svm_model = SVC(kernel = "rbf", random_state = 42)
svm_model.fit(x_train_scaled, y_train)
svm_pred = svm_model.predict(x_test_scaled)
svm_acc = accuracy_score(y_test, svm_pred)
print(f"SVM Accuracy: {svm_acc:.3f}")

print("=" * 60)

print("\nSVM Classification Report:")
print(classification_report(y_test, svm_pred, target_names = cancer.target_names))

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

ConfusionMatrixDisplay.from_predictions(y_test, tree_pred, ax=axes[0], display_labels=cancer.target_names)
axes[0].set_title(f"Decision Tree\nAccuracy: {tree_acc:.3f}")

ConfusionMatrixDisplay.from_predictions(y_test, forest_pred, ax=axes[1],display_labels=cancer.target_names)
axes[1].set_title(f"Random Forest\nAccuracy: {forest_acc:.3f}")

ConfusionMatrixDisplay.from_predictions(y_test, svm_pred, ax=axes[2],display_labels=cancer.target_names)
axes[2].set_title(f"SVM\nAccuracy: {svm_acc:.3f}")

plt.tight_layout()
plt.show()

print("\n" + "=" * 60)
print("Final Comparison:")
print(f"Decision Tree: {tree_acc:.3f}")
print(f"Random Forest: {forest_acc:.3f}")
print(f"SVM:           {svm_acc:.3f}")
print(f"\nWinner: {max([('Tree', tree_acc), ('Forest', forest_acc), ('SVM', svm_acc)], key=lambda x: x[1])[0]}")