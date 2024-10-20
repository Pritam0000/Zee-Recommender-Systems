import pandas as pd

def load_and_preprocess_data():
    # Load datasets
    movies = pd.read_csv('zee-movies.dat', sep='::', engine='python', encoding='latin-1', 
                         names=['movieId', 'title', 'genres'])
    
    ratings = pd.read_csv('zee-ratings.dat', sep='::', engine='python', 
                          names=['userId', 'movieId', 'rating', 'timestamp'])
    
    users = pd.read_csv('zee-users.dat', sep='::', engine='python', encoding='latin-1', 
                        names=['userId', 'gender', 'age', 'occupation', 'zipcode'])

    # Convert data types after loading
    movies['movieId'] = pd.to_numeric(movies['movieId'], errors='coerce')
    ratings['userId'] = pd.to_numeric(ratings['userId'], errors='coerce')
    ratings['movieId'] = pd.to_numeric(ratings['movieId'], errors='coerce')
    ratings['rating'] = pd.to_numeric(ratings['rating'], errors='coerce')
    ratings['timestamp'] = pd.to_numeric(ratings['timestamp'], errors='coerce')
    users['userId'] = pd.to_numeric(users['userId'], errors='coerce')
    users['age'] = pd.to_numeric(users['age'], errors='coerce')
    users['occupation'] = pd.to_numeric(users['occupation'], errors='coerce')

    # Drop rows with NaN values after conversion
    movies = movies.dropna(subset=['movieId'])
    ratings = ratings.dropna()
    users = users.dropna(subset=['userId'])

    # Preprocess data
    movies['year'] = movies['title'].str.extract(r'\((\d{4})\)').astype('float').astype('Int64')
    movies['title'] = movies['title'].str.replace(r'\s*\(\d{4}\)\s*$', '', regex=True).str.strip()

    return movies, ratings, users