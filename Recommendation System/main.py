import pandas as pd
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample movie dataset
dataset = {
    "title" : ["The Shawshank Redemption","The Godfather","The Dark Knight", "Pulp Fiction", "The Lord of the Rings : The Return of the King"],
    "description" : [
        "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
        "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
        "When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham.",
        "The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
        "Gandalf and Aragorn lead the World of Men against Sauron\'s army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring."
        ]
}

movies_dataframe = pd.DataFrame(dataset)
print(movies_dataframe.head())

# Download stopwords
nltk.download("stopwords")
stop_words = stopwords.words("english")

# TF and IDF Vectorizer
tfidf = TfidfVectorizer(stop_words = stop_words)
tfidf_matrix = tfidf.fit_transform(movies_dataframe["description"])

print(tfidf_matrix.shape)

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
print(cosine_sim)

def get_recommendations(title, cosine_sim = cosine_sim):

    # Get the index of the movie that matches the title
    idx = movies_dataframe.index[movies_dataframe["title"] == title].tolist()[0]

    # Get the pairwise similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key = lambda x: x[1], reverse = True)

    # Get the scores of the 5 most similar movies
    sim_scores = sim_scores[1:6]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 5 most similar movies
    return movies_dataframe["title"].iloc[movie_indices]

# Test the Recommendation System
print(get_recommendations("The Godfather"))