import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def data_cleaning_tool(dataframe):

    # Fill missing values in "age" column with the mean age
    dataframe["age"] = dataframe["age"].fillna(dataframe["age"].mean())
    
    # Drop rows with missing values in the "embarked" column
    dataframe = dataframe.dropna(subset = ["embarked"])

    # Normalize the "fare" column
    scaler = MinMaxScaler()
    dataframe["fare"] = scaler.fit_transform(dataframe[["fare"]])

    # Remove duplicate rows
    dataframe = dataframe.drop_duplicates()

    return dataframe

#Dataset
dataset = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
dataframe = pd.read_csv(dataset)

cleaned_dataframe = data_cleaning_tool(dataframe)
print(cleaned_dataframe.head())