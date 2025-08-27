import pandas as pd
import plotly.express as px
from google.cloud import bigquery

# Connect to BigQuery
project_id = 'YOU WISH HAHAHAH'
client = bigquery.Client(project = project_id)

# Define the SQL query to fetch search trend data
query = """
    SELECT
        term,
        score,
        week,
        country_name
    FROM
        `bigquery-public-data.google_trends.international_top_rising_terms`
    WHERE
        term = "Video games" AND country_name IN ("United States", "Philippines")
    ORDER BY
        week DESC
    LIMIT 200
"""

# Execute query and fetch real time data into DataFrame
print("Fetching data from Google BigQuery...\nThis might take a few minutes.")
try:

    # Use client to run query and convert results to a pandas DataFrame
    query_job = client.query(query) # Start query request
    df = query_job.to_dataframe() # Wait for query to finish

    # Rename columns for clarity in analysis
    df.rename(columns = {"country_name": "country", "score": "search_interest"}, inplace = True)

    print("\nSample Data from BigQuery")
    print(df.head(10))
    print("\n")

except Exception as e:
    print(f"An error occured: {e}")
    print("Please ensure you have authenticated your environment with `gcloud auth application-default login`.")
    exit()

# Data cleaning and preparation
df["date"] = pd.to_datetime(df["week"])

# Exploratory Data Analysis (EDA) and interactive visualization with Plotly
print("Creating interactive plot with Plotly...")

figure = px.line(df,
                 x = "date",
                 y = "search_interest",
                 color = "country",
                 title = "Google Search Trends: [Video games] Search Interest by Country",
                 labels = {"date": "Date", "search_interest": "Search Interest Score"})

# Add markers for better visibility on data points
figure.update_traces(mode = "lines+markers")

# Show the plot in browser
figure.show()




