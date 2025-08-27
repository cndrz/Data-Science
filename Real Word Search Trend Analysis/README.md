This project utilizes Google's BigQuery public datasets to analyze real-world search trends. This Python script collects and visualizes historical search interest for specific terms and countries, providing bountiful insight into consumer behavior and regional differences.

Features

- Real World Data: Directly connects to Google's Bigquery public dataset.
- Interactive Visualization: Generates a linechart using Plotly to visualize search trends over time.
- Data Analysis: Utilizes the Pandas library to clean, transform, and prepare the data.

Prerequisites (libraries I used)

- Google Cloud BigQuery
- Pandas
- Plotly

Authentication

Before running the script, make sure you are authenticated with Google Cloud. To do this, you must install Google Cloud SKD, open it and run the following command in your terminal.

- gcloud auth application-default login

Feel free to modify the query terms and countries



