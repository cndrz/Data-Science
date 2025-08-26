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
dataset = pd.read_csv(r"C:\Users\admin\Desktop\Data-Science\Churn Prediction\Telco.csv")

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

# Drop non-numeric columns that are not useful for the model (e.g., 'customerID')
dataset = dataset.drop(['customerID'], axis = 1)

# Encode categorical columns to numerical using one-hot encoding
dataset = pd.get_dummies(dataset, drop_first = True)

# Standardize numerical features
scaler = StandardScaler()
numerical_features = dataset.select_dtypes(include = ["float64", "int64"]).columns
dataset[numerical_features] = scaler.fit_transform(dataset[numerical_features])

# Define features and target variable
x = dataset.drop("Churn_Yes", axis = 1)
y = dataset["Churn_Yes"]

# Plot the distribution of the target variable
plt.figure(figsize = (8, 6))
sns.countplot(x = "Churn_Yes", data = dataset)
plt.title("Distribution of Churn")
plt.show()

# Example: Visualize churn by gender
plt.figure(figsize = (10, 6))
sns.countplot(x = "gender_Male", hue = "Churn_Yes", data = dataset)
plt.title("Churn by Gender")
plt.show()
# Example: Churn by contract type
plt.figure(figsize = (12, 6))
sns.countplot(x = "Contract_Two year", hue = "Churn_Yes", data = dataset)
plt.title("Churn by Contract Type")
plt.show()

# Exclude non-numerical columns
numerical_data = dataset.select_dtypes(include = ["float64", "int64"])

# Compute the correlation matrix
corr_matrix = numerical_data.corr()

# Plot the heatmap of correlations
plt.figure(figsize = (12, 10))
sns.heatmap(corr_matrix, annot = True, cmap = "coolwarm", fmt = ".2f")
plt.title("Correlation Matrix")
plt.show()

# Example: Pair plot for selected features
selected_features = ["MonthlyCharges", "TotalCharges", "tenure", "Churn_Yes"]
sns.pairplot(dataset[selected_features], hue = "Churn_Yes")
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
    "solver": ["liblinear", "lbfgs"]
}

# Initialize GridSearchCV
grid_search = GridSearchCV(LogisticRegression(), param_grid, cv = 5, scoring = "accuracy")

# Fit GridSearchCV
grid_search.fit(x_train, y_train)

# Best parameters and best score
print(f"Best Parameters: {grid_search.best_params_}")
print(f"Best Score: {grid_search.best_score_}")

# Optional - Save the model
# joblib.dump(model, "Churn_Prediction_Model.pkl")
