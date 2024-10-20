import pandas as pd

def get_top_rated_movies(movies, ratings, n=10):
    # Calculate average rating for each movie
    movie_ratings = ratings.groupby('movieId')['rating'].agg(['mean', 'count'])
    # Filter movies with at least 100 ratings
    popular_movies = movie_ratings[movie_ratings['count'] >= 100].sort_values('mean', ascending=False)
    # Get top N movies
    top_movies = movies[movies['movieId'].isin(popular_movies.head(n).index)]
    return top_movies['title'].tolist()

def get_user_demographics(users):
    # Calculate user demographics
    gender_dist = users['gender'].value_counts(normalize=True)
    age_dist = users['age'].value_counts(normalize=True).sort_index()
    occupation_dist = users['occupation'].value_counts(normalize=True)
    return gender_dist, age_dist, occupation_dist