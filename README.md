# Movie-Recommender

## Business Understanding
In this project we address the needs of a hypothetical movie streaming business looking to increase revenue. The business is new to online streaming and wants to compete with larger well known online streaming businesses.  Using the MovieLens dataset and well established data science techniques we build movie recommendation engines using both collaborative and content based filtering. The assumption is that by accurately predicting sound movie recommendations to subscribers, subscribers will stay on the streaming platform longer and remain customers longer. It can also present an opportunity for ad based revenue targeting customers on the platform. Furthermore, satisfied customers are more likely to recommend the streaming service to family and friends. 

## Data Understanding
The data set used for this project is the MovieLens dataset from the GroupLens research lab at the University of Minnesota. It contains 100,835 unique viewer ratings, 610 individual viewers, and 9,724 movies.

### The Data
The dataset is a clean dataset containing four CSV files:
1. `links.csv` (9742, 3)
Is a csv file containing 3 columns, `movieId`, `imdbId`, `tmdbId` with 9742 rows. Each row represents a unique movie.
2. `movies.csv` (9742, 3)
Is a csv file containing 3 columns, `movieId`, `title`, and `genre` with 9742 rows. Each row represents a unique movie
3. `ratings.csv` (100836, 4)
Is a csv file containg 4 `columns`, `userId`,	`movieId`, `rating`, `timestamp` with 100836 rows. Each row represents a `rating` from a `userID` assigned to a `movieID`
4. `tags.csv` (3683, 4)
Is a csv file containing 4 columns, `userId`,	`movieId`,	`tag`,	`timestamp` with 2683 rows. Each row represents a `timestamp` a `userID` gave assigned a `movieID` a `tag`.

## Preparing the Data
CSV files are converted to both Pandas and Spark data frames, and are extensively used in this project. Data frames are merged together in advance of modeling. We conduct a train-test split separating data into training and testing sets for model training and evaluation. 

## The Model
The primary predictive model used in this project is Apache Spark ML Alternating Least Squares (ALS) for collaborative filtering. ALS recommender is a matrix factorization algorithm that uses Alternating Least Squares with Weighted-Lamda-Regularization (ALS-WR). It uses matrix multiplication with user ratings. As there are a lot of blank ratings (not every user has rated every movie), it predicts ratings for those blanks and recommneds movies based on those predictions. Our ALS model predicts top 5 rated movies for each user. We also build custom content based filtering predictive engines using Python.
Need to fit this into the paragraph. After building our first simple model, and adjusting parameters, we run a param grid to identify the best performing model. 

### Model Evaluation
Why did we pick RMSE? It's the industry standard.
The ALS model is evaluated using the RMSE (Root Mean Squared Error) metric and our model’s RMSE score is 0.86 which is consistent with other published ALS recommender engines where the same dataset is used.

## Business Deployment
We optimize our model to recommend five movies for our users, based on their past rating history.
The infographic bellow shows some examples of movies our recommender suggests given a `liked` rating for the movie.

## Summary
In summary our model produces...

