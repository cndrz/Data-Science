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
print(f"\nShape: {df.shape:}")
print(f"Churn Distribution:\n{df["Churn"].value_counts()}")

df = df.drop("customer_ID", axis = 1)

df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors = "coerce")
df = df.dropna()

df["Churn"]