import streamlit as st
import pandas as pd
from data_loader import load_and_preprocess_data
from recommender import get_movie_recommendations

st.title("Movie Recommender System")

# Load and preprocess data
try:
    movies, ratings, users = load_and_preprocess_data()
    
    # Basic data validation
    if movies.empty or ratings.empty or users.empty:
        raise ValueError("One or more datasets are empty")
    
    st.success("Data loaded successfully!")
except Exception as e:
    st.error(f"Error loading data: {str(e)}")
    st.error("Please check your data files and ensure they are in the correct format.")
    st.stop()

# Display some basic statistics
st.write(f"Number of movies: {len(movies)}")
st.write(f"Number of ratings: {len(ratings)}")
st.write(f"Number of users: {len(users)}")

# Display data types
st.write("Data types:")
st.write(movies.dtypes)
st.write(ratings.dtypes)
st.write(users.dtypes)

# User input
st.header("Rate some movies")
user_ratings = {}
for _ in range(5):
    col1, col2 = st.columns(2)
    with col1:
        movie = st.selectbox(f"Select movie {_+1}", movies['title'].tolist(), key=f"movie_{_}")
    with col2:
        rating = st.slider(f"Rate movie {_+1}", 1, 5, 3, key=f"rating_{_}")
    if movie:
        movie_id = movies[movies['title'] == movie]['movieId'].values[0]
        user_ratings[movie_id] = rating

if st.button("Get Recommendations"):
    if user_ratings:
        try:
            recommendations = get_movie_recommendations(user_ratings, movies, ratings)
            st.header("Recommended Movies")
            for movie in recommendations:
                st.write(f"- {movie}")
        except Exception as e:
            st.error(f"Error generating recommendations: {str(e)}")
    else:
        st.warning("Please rate at least one movie to get recommendations.")