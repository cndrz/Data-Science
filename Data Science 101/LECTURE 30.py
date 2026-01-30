import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay
import kagglehub

path = kagglehub.dataset_download("blastchar/telco-customer-churn")
df = pd.read_csv(f"{path}/WA_Fn-UseC_-Telco-Customer-Churn.csv")

print("Dataset Preview:")
print(df.head())
<<<<<<< HEAD
print(f"\nShape: {df.shape}")
print(f"Churn distribution:\n{df['Churn'].value_counts()}")

df = df.drop("customerID", axis = 1)
=======
print(f"\nShape: {df.shape:}")
print(f"Churn Distribution:\n{df["Churn"].value_counts()}")

df = df.drop("customer_ID", axis = 1)
>>>>>>> 188cae13c0fd795dbe4274db8960b55cc86edd55

df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors = "coerce")
df = df.dropna()

<<<<<<< HEAD
df["Churn"] = (df["Churn"] == "Yes").astype(int)

categorical_cols = df.select_dtypes(include = ["object"]).columns
df_encoded = pd.get_dummies(df, columns = categorical_cols, drop_first = True)

x = df_encoded.drop("Churn", axis = 1)
y = df_encoded["Churn"]

print(f"\nAfter preprocessing: {x.shape}")

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

print("\n" + "=" * 60)
print("PART 1: Default Parameters (No Tuning)")
print("=" * 60)

models_default = {

    "KNN": KNeighborsClassifier(),
    "Random Forest": RandomForestClassifier(random_state = 42),
    "SVM": SVC(random_state = 42)

}

default_results = {}

for name, model in models_default.items():

    model.fit(x_train_scaled, y_train)
    pred = model.predict(x_test_scaled)
    acc = accuracy_score(y_test, pred)
    default_results[name] = acc
    print(f"{name:15} Accuracy: {acc:.3f}")

print("\n" + "=" * 60)
print("PART 2: GridSearchCV (Automatic Tuning)")
print("=" * 60)

param_grids = {

    "KNN": {

        "n_neighbors": [3, 5, 7, 9, 11, 13, 15],
        "weights": ["uniform", "distance"]

    },

    "Random Forest": {

        "n_estimators": [50, 100, 200],
        "max_depth": [10, 20, None],
        "min_samples_split": [2, 5, 10]

    },

    "SVM": {

        "C": [0.1, 1, 10],
        "kernel": ["linear", "rbf"],
        "gamma": ["scale", "auto"]
    }

}

tuned_results = {}
best_models = {}

for name in ["KNN", "Random Forest", "SVM"]:
    print(f"\nTuning {name}...")

    grid_search = GridSearchCV(

        estimator = models_default[name].__class__(random_state = 42) if name != "KNN" else KNeighborsClassifier(),
        param_grid = param_grids[name],
        cv = 5,
        scoring = "accuracy",
        n_jobs = 1,
        verbose = 1
    )

    grid_search.fit(x_train_scaled, y_train)

    print(f"Best Parameters: {grid_search.best_params_}")
    print(f"Best CV Score: {grid_search.best_score_:.3f}")

    best_pred = grid_search.predict(x_test_scaled)
    test_acc = accuracy_score(y_test, best_pred)
    tuned_results[name] = test_acc
    best_models[name] = grid_search.best_estimator_

    print(f"Test set accuracy: {test_acc:.3f}")

print("\n" + "=" * 60)
print("FINAL COMPARISON: Default vs Tuned")
print("=" * 60)

comparison_df = pd.DataFrame({

    "Default": default_results,
    "Tuned": tuned_results,
    "Improvements": {k: tuned_results[k] - default_results[k] for k in default_results.keys()}

})

print(comparison_df)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (14, 5))

x = np.arange(len(default_results))
width = 0.35

ax1.bar(x - width/2, list(default_results.values()), width, label = "Default", alpha = 0.8)
ax1.bar(x + width/2, list(tuned_results.values()), width, label = "Tuned", alpha = 0.8)
ax1.set_ylabel("Accuracy")
ax1.set_title("Default vs Tuned Parameters")
ax1.set_xticks(x)
ax1.set_xticklabels(default_results.keys())
ax1.legend()
ax1.grid(True, alpha = 0.3)

improvements = [tuned_results[k] - default_results[k] for k in default_results.keys()]
colors = ["green" if i > 0 else "red" for i in improvements]
ax2.bar(default_results.keys(), improvements, color=colors, alpha=0.7)
ax2.set_ylabel("Accuracy Improvement")
ax2.set_title("Improvement from Tuning")
ax2.axhline(y = 0, color = "black", linestyle = "-", linewidth = 0.5)
ax2.grid(True, alpha = 0.3)

plt.tight_layout()
plt.show()

print("\n" + "=" * 60)
print("Best Overall Model Performance")
print("=" * 60)

best_overall = max(tuned_results, key=tuned_results.get)
print(f"Winner: {best_overall} with {tuned_results[best_overall]:.3f} accuracy")

best_pred = best_models[best_overall].predict(x_test_scaled)
print("\nClassification Report:")
print(classification_report(y_test, best_pred, target_names = ["Stay", "Churn"]))

ConfusionMatrixDisplay.from_predictions(y_test, best_pred, display_labels = ["Stay", "Churn"])
plt.title(f"Best Model: {best_overall}\nAccuracy: {tuned_results[best_overall]:.3f}")
plt.show()
=======
df["Churn"]
>>>>>>> 188cae13c0fd795dbe4274db8960b55cc86edd55
