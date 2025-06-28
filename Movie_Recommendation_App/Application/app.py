from flask import Flask, render_template, request, jsonify
from recommendation_engine import MovieRecommender

app = Flask(__name__)
recommender = MovieRecommender('movie_data.csv')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/recommend', methods=['POST'])
def recommend():
    movie_title = request.json.get('movie', '')
    recommendations = recommender.get_recommendations(movie_title)
    return jsonify(recommendations)


if __name__ == '__main__':
    app.run(debug=True)
