# Movie-Recommender

## Understanding the Problem
Flatflix is an hypothetical Netflix competitor that is all about connecting people to the movies they love. To help customers find those movies, they want to develop a world-class movie recommendation system to encourage users to stay on the platform. The movie recommender well recommend movie to users using a collaborative apporach. Users will be shown movies that similar users have liked in the past, we will also address the "Cold Start" problem of users with no history on the platform.

## Understanding The Data
We will be using the MovieLens dataset from the GroupLens research lab at the University of Minnesota. Becuase we are not planning on running our analysis on a powerful enough cloud platform, we will use the "small" dataset containing 100,000 user ratings.

The MovieLens dataset is a "classic" recommendation system dataset, that is used in numerous academic papers and machine learning proofs-of-concept. You will need to create the specific details about how the user will provide their ratings of other movies, in addition to formulating a more specific business problem within the general context of "recommending movies".

The dataset was a clean dataset containing four CSV files:
1. links.csv (9742, 3)
Is a csv file containing 3 columns, MovieId, imdbId, tmdbId with 9742 rows. Each row is a unique movie.
2. movies.csv (9742, 3)
Is a csv file containing 3 columns, movieId, title, and genre with 9742 rows. Each row is a unique movie
3. ratings.csv (100836, 4)
Is a csv file containg 4 columns, userId,	movieId, rating, timestamp with 100836. Each row is a rating from a userID assigned to a movieID
4. tags.csv (3683, 4)
Is a csv file containing 3683

## Preparing the Data

## The Model

## Model Evaluation

## Business Deployment

## Summary
