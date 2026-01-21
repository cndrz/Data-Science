import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

from sklearn.datasets import load_diabetes
diabetes = load_diabetes()

x = diabetes.data
y = (diabetes.target > np.median(diabetes.target)).astype(int)

print(f"Dataset Shape: {x.shape}")
print(f"Class Distribution: {np.bincount(y)}")

print("\n" + "=" * 60)
print("THE OLD WAY: Single Train/Test Split")
print("=" * 60)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

models = {

    "KNN": KNeighborsClassifier(n_neighbors = 5),
    "Random Forest": RandomForestClassifier(n_estimators = 100, random_state = 42),
    "SVM": SVC(kernel = "rbf", random_state = 42)

}

for name, model in models.items():

    model.fit(x_train_scaled, y_train)
    pred = model.predict(x_test_scaled)
    acc = accuracy_score(y_test, pred)
    print(f"{name:15} Accuracy: {acc:.3f}")

print("\n" + "=" * 60)
print("THE NEW WAY: 5-Fold Cross-Validation")
print("=" * 60)

scaler_cv = StandardScaler()
x_scaled = scaler_cv.fit_transform(x)

for name, model in models.items():

    scores = cross_val_score(model, x_scaled, y, cv = 5)
    mean_acc = scores.mean()
    std_acc = scores.std()

    print(f"{name:15} Accuracy: {mean_acc:.3f} ± {std_acc:.3f}")
    print(f"Individual folds: {scores}")

print("\n" + "=" * 60)
print("COMPARISON: Single Split vs Cross-Validation")
print("=" * 60)

single_split_results = {name: [] for name in models.keys()}

for seed in range(10):

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = seed)
    scaler_temp = StandardScaler()
    x_train_scaled = scaler_temp.fit_transform(x_train)
    x_test_scaled = scaler_temp.transform(x_test)

    for name, model in models.items():

        model_temp = model.__class__(**model.get_params())
        model_temp.fit(x_train_scaled, y_train)
        acc = accuracy_score(y_test, model_temp.predict(x_test_scaled))
        single_split_results[name].append(acc)

fig, axes = plt.subplots(1, 3, figsize = (15, 5))

for idx, (name, model) in enumerate(models.items()):
    # Single split variability
    single_accs = single_split_results[name]
    
    # CV score
    cv_scores = cross_val_score(model, x_scaled, y, cv=5)
    
    axes[idx].boxplot([single_accs, [cv_scores.mean()]* 5], tick_labels=["10 Random Splits", "5-Fold CV (avg)"])
    axes[idx].set_ylabel("Accuracy")
    axes[idx].set_title(f"{name}\nCV: {cv_scores.mean():.3f} ± {cv_scores.std():.3f}")
    axes[idx].grid(True, alpha = 0.3)

plt.tight_layout()
plt.show()

print("\nKey Insight: Cross-validation gives you a more stable,")
print("reliable estimate of your model's true performance!")