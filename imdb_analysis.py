from imdbpie import Imdb
from nltk.sentiment.vader import SentimentIntensityAnalyzer

imdb = Imdb()
sentIA = SentimentIntensityAnalyzer()
popular_movies = imdb.popular_movies()
movies = []

class Movie:
    """represents a movie object"""

def populate_movies():
    """populate the movies array with information on each popular new movie"""
    for i in range(len(popular_movies)):
        movie_obj = popular_movies[i]['object']

        new_movie = Movie()
        new_movie.id = movie_obj['tconst']
        new_movie.title = movie_obj['title']
        new_movie.reviews = imdb.get_title_reviews(new_movie.id, max_results=25)
        new_movie.sentiment = analyze_reviews_sentiment(new_movie)
        movies.append(new_movie)

def analyze_reviews_sentiment(film):
    """return the result of a sentiment analysis on a movie's reviews"""
    review = "No reviews yet"
    if film.reviews is None:
        return review
    else:
        for i in range(len(film.reviews)):
            review += film.reviews[i].text
    return sentIA.polarity_scores(review)

populate_movies()

for j in range(len(movies)):
    print(movies[j].title + " has a sentiment analysis of: " + str(movies[j].sentiment))

# print(imdb.search_for_title("The Dark Knight")[0])
# print(imdb._get_reviews_data("tt0468569")[0]['summary'])
# print(imdb._get_reviews_data("tt0468569")[0]['user_name'])
# print(imdb._get_reviews_data("tt0468569")[0]['date'])
# print(imdb._get_reviews_data("tt0468569")[0]['text'])