import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

iris = load_iris()
x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

k_values = range(1, 31)
accuracies = []

for k in k_values:
    
    model = KNeighborsClassifier(n_neighbors = k)
    model.fit(x_train_scaled, y_train)

    accuracy = model.score(x_test_scaled, y_test)
    accuracies.append(accuracy)

plt.figure(figsize = (10, 6))
plt.plot(k_values, accuracies, marker = "x", linestyle = "-", color = "b")
plt.xlabel("Number of Neighbors (K)")
plt.ylabel("Accuracy")
plt.title("Elbow Method: Finding Optimal K")
plt.grid(True)
plt.show()

optimal_k = 5

final_model = KNeighborsClassifier(n_neighbors = optimal_k)
final_model.fit(x_train_scaled, y_train)
y_pred = final_model.predict(x_test_scaled)

print(f"Optimal K: {optimal_k}")
print(f"Final Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print(f"\nClassification Report: ")
print(classification_report(y_test, y_pred))

