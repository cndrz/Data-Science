import requests
import pandas as pd
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns

# Replace with your own NewsAPI key
api_key = "d8fb30f465354a00b238b1f7a3e1fa27"

# Function to fetch news articles
def fetch_news(query, page_size=100):
    url = f"https://newsapi.org/v2/everything?q={query}&pageSize={page_size}&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    articles = data["articles"]
    news_list = [[article["publishedAt"], article["title"], article["description"], article["content"]] for article in articles]
    news_dataframe = pd.DataFrame(news_list, columns = ["Datetime", "Title", "Description", "Content"])
    return news_dataframe

# Function to clean text
def clean_text(text):
    if text:
        text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE)
        text = re.sub(r'\@\w+|\#','', text)
        text = re.sub(r'[^\w\s]', '', text)
        text = text.lower()
        return text
    return ""

# Function to get sentiment using VADER
def get_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_score = analyzer.polarity_scores(text)
    if sentiment_score['compound'] >= 0.05:
        return "Positive"
    elif sentiment_score['compound'] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# Fetch and clean news articles
query = "Philippines"
news_dataframe = fetch_news(query, page_size = 100)
news_dataframe["Cleaned Content"] = news_dataframe["Content"].apply(clean_text)

# Apply sentiment analysis
news_dataframe["Sentiment"] = news_dataframe["Cleaned Content"].apply(get_sentiment)
print(news_dataframe.head(10))

# Visualize the results
plt.figure(figsize = (8, 6))
sns.countplot(x = "Sentiment", hue = "Sentiment", data = news_dataframe, palette = "viridis", legend = False)
plt.title("Sentiment Analysis of News Articles")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.show()
