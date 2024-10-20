import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def get_movie_recommendations(user_ratings, movies, ratings):
    # Create user-item matrix
    user_item_matrix = ratings.pivot(index='userId', columns='movieId', values='rating')
    
    # Add the new user's ratings
    new_user_id = user_item_matrix.index.max() + 1
    user_item_matrix.loc[new_user_id] = pd.Series(user_ratings)

    # Calculate item-item similarity
    item_similarity = cosine_similarity(user_item_matrix.T.fillna(0))
    
    # Get similar movies
    similar_movies = pd.DataFrame(item_similarity, index=user_item_matrix.columns, columns=user_item_matrix.columns)
    
    # Calculate weighted average of similar movies
    user_ratings_series = pd.Series(user_ratings)
    similar_movies_weighted = similar_movies.loc[user_ratings_series.index].T.mul(user_ratings_series, axis=1)
    similar_movies_weighted_sum = similar_movies_weighted.sum(axis=1)
    
    # Sort and get top recommendations
    recommendations = similar_movies_weighted_sum.sort_values(ascending=False).head(10)
    
    # Get movie titles
    recommended_movies = movies[movies['movieId'].isin(recommendations.index)]['title'].tolist()
    
    return recommended_movies