import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno

def eda(dataframe):

    # Display first few rows of the dataset
    print(f"FIRST 5 ROWS OF THE DATASET:\n\n{dataframe.head()}\n")

    # Basic Statistics
    print(f"SUMMARY STATISTICS:\n\n{dataframe.describe()}\n")

    # Dataset Information
    print("DATAFRAME INFORMATION:\n")
    dataframe.info()
    print("\n")

    # Missing Value Visualization
    print(f"MISSING VALUES:\n\n{dataframe.isnull().sum()}\n")
    msno.heatmap(dataframe)
    plt.show()

    # Distribution plots for numerical columns
    numerical_columns = dataframe.select_dtypes(include = ["float64", "int64"]).columns
    for col in numerical_columns:
        plt.figure(figsize = (10, 6))
        sns.histplot(dataframe[col], kde=True)
        plt.title(f"Distribution of {col}")
        plt.show()

    # Box plots for numerical columns
    for col in numerical_columns:
        plt.figure(figsize = (10, 6))
        sns.boxplot(x = dataframe[col])
        plt.title(f"Box Plot of {col}")
        plt.show()

    # Bar plots for categorical columns
    categorical_columns = dataframe.select_dtypes(include = ["object"]).columns
    for col in categorical_columns:
        plt.figure(figsize = (10, 6))
        sns.countplot(y = dataframe[col])
        plt.title(f"Count Plot of {col}")
        plt.show()

    # Frequency tables for categorical columns
    for col in categorical_columns:
        print(f"FREQUENCY TABLE FOR {col.upper()}:\n\n{dataframe[col].value_counts()}\n")

    # Correlation heatmap
    plt.figure(figsize=(12, 8))
    correlation_matrix = dataframe.select_dtypes(include = ["float64", "int64"]).corr()
    sns.heatmap(correlation_matrix, annot = True, cmap = "coolwarm", linewidths=0.5)
    plt.title("Correlation Heatmap")
    plt.show()

    # Pair plot for pairwise relationships
    sns.pairplot(dataframe.select_dtypes(include = ["float64", "int64"]).dropna())
    plt.show()

# Sample Dataset
dataset = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
dataframe = pd.read_csv(dataset)

eda(dataframe)
