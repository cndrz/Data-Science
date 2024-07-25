import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load sample dataset
path = "Health Data Analysis/diabetes.csv"
dataset = pd.read_csv(path)

# Display basic information about the dataset
print(dataset.info)
print(dataset.describe())
print(dataset.head())

# Data cleaning and preprocessing
# Check for missing values
print(dataset.isnull().sum())

# Handle missing values if there is any
dataset = dataset.fillna(method = "ffill")

# Exploratory Data Analysis (EDA)
sns.pairplot(dataset, hue = "Outcome")
plt.show()

# Split data into features and target
x = dataset.drop("Outcome", axis = 1) # Replace "Outcome" with the target variable
y = dataset["Outcome"]

# Split data into training and test sets 
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 42)

# Standardize the data
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# Train a logistics regression model
model = LogisticRegression()
model.fit(x_train, y_train)

# Make predictions
y_pred = model.predict(x_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print(f"Classification Report: \n {classification_report(y_test, y_pred)}")
print(f"Confusion Matrix: \n {confusion_matrix(y_test, y_pred)}")

# Save the model (OPTIONAL)
""" import joblib
joblib.dump(model, "Health Model.pkl") """
