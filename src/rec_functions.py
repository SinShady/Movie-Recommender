import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def combine_features(row):
    return row['genres'] +" "+row['combined_tags']

def get_title_from_index(df, index):
    return df[df.index == index]["title"].values[0]

def get_index_from_title(df, title):
    return df[df.title == title].index[0]

def get_title_from_movie_id(df, movie_id):
    return df[df.movieId == movie_id]["title"].values[0]

def similar_movies(df, title):
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(df["combined_features"])
    cosine_sim = cosine_similarity(count_matrix)
    movie_index = get_index_from_title(df, title)
    similar_movies =  list(enumerate(cosine_sim[movie_index]))
    sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)[1:]
    i=0
    
    print("\nTop 5 similar movies to "+title+" are:\n")
    
    for element in sorted_similar_movies:
        print(get_title_from_index(df, element[0]))
        i=i+1
        if i>=5:
            break

def newbayes_ucb1_policy(df, ucb_scale=2.0):
    '''
    Applies Bayesian UCB policy to generate movie recommendations
    Args:
        df: dataframe. Dataset to apply Bayesian UCB policy to.
        ucb_scale: float. Most implementations use 2.0.
    '''
    scores = df[['movieId', 'liked']].groupby('movieId').agg({'liked': ['mean', 'count', 'std']})
    scores.columns = ['mean', 'count', 'std']
    scores['ucb'] = scores['mean'] + (ucb_scale * scores['std'] / np.sqrt(scores['count']))
    scores['movieId'] = scores.index
    scores = scores.sort_values('ucb', ascending=False)
    recs = scores.loc[scores.index[0:6], 'movieId'].values
    movie_name = []
    for movieid in recs:
        movie_name.append(get_title_from_movie_id(df, movieid))
    return movie_name