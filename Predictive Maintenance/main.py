import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
dataset = pd.read_csv("maintenance.csv")

# Display the first few rows of the dataset
print(dataset.head())

# Check for missing values
print(dataset.isnull().sum())

# Basic statistics
print(dataset.describe())

# Handle missing values
# Example: Filling missing values with the mean
dataset.fillna(dataset.mean(), inplace = True)

# Feature engineering (example)
# Creating new features based on existing data
dataset["feature_x"] = dataset["metric1"] * dataset["metric2"]

# Drop non-numeric columns that won't be used in the model
dataset = dataset.drop(columns = ["date", "device"])

# Normalize/Standardize data if necessary
scaler = StandardScaler()
data_scaled = scaler.fit_transform(dataset.drop("failure", axis = 1))

# Convert scaled data back to DataFrame
data_scaled = pd.DataFrame(data_scaled, columns = dataset.columns[:-1])

# Add the target column back
data_scaled["failure"] = dataset["failure"]

# Correlation matrix
plt.figure(figsize = (12, 8))
sns.heatmap(data_scaled.corr(), annot = True, cmap = "coolwarm")
plt.show()

# Pair plot
sns.pairplot(dataset, vars = ['metric1', 'metric2', 'metric3', 'metric4'], hue = "failure")
plt.show()

# Split the data into training and testing sets
x = data_scaled.drop("failure", axis = 1)
y = data_scaled["failure"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 42)

# Train a random forest classifier
rf_model = RandomForestClassifier(n_estimators = 100, random_state = 42)
rf_model.fit(x_train, y_train)

# Predictions
y_pred = rf_model.predict(x_test)
y_prob = rf_model.predict_proba(x_test)[:, 1]

# Model evaluation
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
print(f"ROC AUC Score: {roc_auc_score(y_test, y_prob)}")
