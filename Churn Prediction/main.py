import joblib
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# Load the dataset
dataset = pd.read_csv("Telco.csv")

# Display the first few rows of the dataset
print(dataset.head())

# Basic information about the dataset
print(dataset.info())

# Summary statistics
print(dataset.describe(include = "all"))

# Check for missing values
print(dataset.isnull().sum())

# Handling missing values (drop rows with missing values)
dataset.dropna(inplace = True)

# Standardize numerical features
scaler = StandardScaler()
numerical_features = dataset.select_dtypes(include = ["float64", "int64"]).columns
dataset[numerical_features] = scaler.fit_transform(dataset[numerical_features])

# Define features and target variable
x = dataset.drop("Churn", axis = 1)
y = dataset["Churn"]

# Plot the distribution of the target variable
plt.figure(figsize = (8, 6))
sns.countplot(x = "Churn", data = dataset)
plt.title("Distribution of Churn")
plt.show()

# Example: Visualize churn by gender
plt.figure(figsize = (10, 6))
sns.countplot(x = "gender", hue = "Churn", data = dataset)
plt.title("Churn by gender")

# Example: Churn by contract type
plt.figure(figsize = (12, 6))
sns.countplot(x = "Contract", hue = "Churn", data = dataset)
plt.title("Churn by Contract Type")
plt.show()

# Compute the correlation matrix
corr_matrix = dataset.corr()

# Plot the heatmap of correlations
plt.figure(figsize = (12, 10))
sns.heatmap(corr_matrix, annot = True, cmap = "Coolwarm", fmt = ".2f")
plt.title("Correlation Matrix")
plt.show()

# Example: Pair plot for selected features
selected_features = ["Monthly Charges", "Total Charges", "Tenure", "Churn"]
sns.pairplot(dataset[selected_features], hue = "Churn")
plt.show()

# Train a random forest model to get feature importance
model = RandomForestClassifier()
model.fit(x, y)

# Get feature importance
importance = model.feature_importances_

# Create a data frame for feature importance
feature_importance = pd.DataFrame({"Feature": x.columns, "Importance": importance})
feature_importance = feature_importance.sort_values(by = "Importance", ascending = False)

# Plot feature importance
plt.figure(figsize = (12, 8))
sns.barplot(x = "Importance", y = "Feature", data = feature_importance)
plt.title("Feature Importance")
plt.show()

# Split the data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 42)

# Initialize and train the model
model = LogisticRegression()
model.fit(x_train, y_train)

# Make predictions
y_pred = model.predict(x_test)

# Evaluate the model
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Apply SMOTE
smote = SMOTE(random_state = 42)
x_resampled, y_resampled = smote.fit_resample(x_train, y_train)

# Train the model on the resampled data
model.fit(x_resampled, y_resampled)

# Make predictions
y_pred = model.predict(x_test)

# Evaluate the model
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Define the parameter grid
param_grid = {
    "C": [0.01, 0.1, 1, 10, 100],
    "Solver": ["Liblinear", "LBFGS"]

}

# Initialize GridSearchCV
grid_search = GridSearchCV(LogisticRegression(), param_grid, cv = 5, scoring = "Accuracy")

# Fit GridSearchCV
grid_search.fit(x_train, y_train)

# Best parameters and best score
print(f"Best Parameters: {grid_search.best_params_}")
print(f"Best score: {grid_search.best_score_}")

# Optional - Save the model
# joblib.dump(model, "Churn Prediction Model.pkl")





