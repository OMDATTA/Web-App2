import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class MovieRecommender:
    def __init__(self, csv_path):
        # Load movie data
        self.movies_df = pd.read_csv(csv_path)

        # Prepare feature matrix
        self.movies_df['combined_features'] = (
            self.movies_df['genres'] + ' ' +
            self.movies_df['keywords'] + ' ' +
            self.movies_df['cast']
        )

        # Create TF-IDF vectorizer
        self.tfidf = TfidfVectorizer(stop_words='english')
        self.feature_matrix = self.tfidf.fit_transform(
            self.movies_df['combined_features'])

    def get_recommendations(self, movie_title, num_recommendations=5):
        # Find the index of the movie
        try:
            movie_index = self.movies_df[self.movies_df['title']
                                         == movie_title].index[0]
        except IndexError:
            return []

        # Compute cosine similarity
        similarity_scores = cosine_similarity(
            self.feature_matrix[movie_index],
            self.feature_matrix
        ).flatten()

        # Get top recommendations
        similar_indices = similarity_scores.argsort()[
            ::-1][1:num_recommendations+1]

        recommendations = self.movies_df.iloc[similar_indices][[
            'title', 'genres', 'vote_average']]
        return recommendations.to_dict('records')
