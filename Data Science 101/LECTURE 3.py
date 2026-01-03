import pandas as pd

engagement_data = {

    "Post_ID" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Likes" : [566, 223, 246, 7434, 6236, 123, 23125, 12512, 12151, 1231]
}

df = pd.DataFrame(engagement_data)

mean_val = df["Likes"].mean()
median_val = df["Likes"].median()
std_val = df["Likes"].std()

summary = df.describe()

print("--- Key Engagement Metrics ---")
print(f"Average Likes: {mean_val:.2f}")
print(f"Median Likes:  {median_val:.2f}")
print(f"Standard Dev:  {std_val:.2f}")
print("\n--- Full Statistical Summary ---")
print(summary)