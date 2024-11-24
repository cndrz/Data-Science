import matplotlib.pyplot as plt

# Sample data: Monthly sales figures
sales = [120, 150, 130, 170, 190, 110, 160, 140, 180, 200, 150, 175]

# Create a Histogram
plt.hist(sales, bins = 5, color = "Red", edgecolor = "Blue")

# Add labels and title
plt.title("Monthly Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")

# Show the plot
plt.show()