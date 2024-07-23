import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load the sample dataset
dataset = pd.read_csv("Customer Segmentation/customers.csv")

# Display dataset basic information
print(dataset.info())

# Display dataset basic statistics
print(dataset.describe())

# Drop dataset missing values
dataset = dataset.dropna()

# Display the cleaned data
print(dataset.head())

# Pairplot to visualize relationships
sns.pairplot(dataset)
plt.show()

# Correlation matrix
plt.figure(figsize = (10, 8))
sns.heatmap(dataset.corr(), annot = True, cmap = "coolwarm")
plt.show

# Standardize the data
scaler = StandardScaler()
scaled_date = scaler.fit_transform(dataset)

# Apply K-Means clustering
kmeans = KMeans(n_clusters = 3) # Change number of clusters if needed
kmeans.fit(scaled_date)

# Add the cluster lables to the original data
dataset["Cluster"] = kmeans.labels_

# Display the clustered data
print(dataset.head())

# Visualize the clusters
plt.figure(figsize = (10, 8))
sns.scatterplot(x = "Feature 1", y = "Feature 2", hue = "Cluster", data = dataset, palette = "viridis")
plt.title("Customer Segments")
plt.show()
