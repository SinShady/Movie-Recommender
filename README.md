# Movie-Recommender

## Business Understanding
In this project we address the needs of a hypothetical movie streaming business looking to increase revenue. The business is new to online streaming and wants to compete with larger well known online streaming businesses.  Using the MovieLens dataset and well established data science techniques we build movie recommendation engines using both collaborative and content based filtering. The assumption is that by accurately predicting sound movie recommendations to subscribers, subscribers will stay on the streaming platform longer and remain customers longer. It can also present an opportunity for ad based revenue targeting customers on the platform. Furthermore, satisfied customers are more likely to recommend the streaming service to family and friends. 

## Data Understanding
The data set used for this project is the MovieLens dataset from the GroupLens research lab at the University of Minnesota. It contains 100,835 unique viewer ratings, 610 individual viewers, and 9,724 movies.

### The Data
The dataset is a clean dataset containing four CSV files:
1. `links.csv` (9742, 3):
Is a csv file containing 3 columns, `movieId`, `imdbId`, `tmdbId` with 9742 rows. Each row represents a unique movie.
2. `movies.csv` (9742, 3):
Is a csv file containing 3 columns, `movieId`, `title`, and `genre` with 9742 rows. Each row represents a unique movie
3. `ratings.csv` (100836, 4):
Is a csv file containg 4 `columns`, `userId`,	`movieId`, `rating`, `timestamp` with 100836 rows. Each row represents a `rating` from a `userID` assigned to a `movieID`
4. `tags.csv` (3683, 4):
Is a csv file containing 4 columns, `userId`,	`movieId`,	`tag`,	`timestamp` with 2683 rows. Each row represents a `timestamp` a `userID` gave assigned a `movieID` a `tag`.

## Preparing the Data
CSV files are imported and converted to both Pandas and Spark data frames, and are extensively used in this project. Data frames are merged together in advance of modeling onthe `movieId` column. We conduct a train-test split separating data into training and testing sets for model training and evaluation on an 80/20 split respectively. 
We also feature engineer a new column named `liked`. This then re-casts our scores from a 0-5 star rating problem to a binary like/no-like problem, with 4.0 stars and above representing a “liked” movie.

## The Model
The primary predictive model used in this project is Apache Spark ML Alternating Least Squares (ALS) for collaborative filtering. ALS recommender is a matrix factorization algorithm that uses Alternating Least Squares with Weighted-Lamda-Regularization (ALS-WR). It uses matrix multiplication with user ratings. As there are a lot of blank ratings (not every user has rated every movie), it predicts ratings for those blanks and recommneds movies based on those predictions. Our ALS model predicts top 5 rated movies for each user. After building our first simple model, and adjusting parameters, we run a param grid to identify the best performing model. We also build custom content based filtering predictive engines using Python. 

### Model Evaluation
Our ALS model is evaluated using the RMSE (Root Mean Squared Error) metric and our model’s RMSE score is 0.86 which is consistent with other published ALS recommender engines where the same dataset is used.

RMSE or Root Mean Squared Error is used as a measure of prediction accuracy. I.e. Given a set of items (movies) how well can the system predict my ratings for these items, or how well it can predict that i will watch these items.
RMSE is typically used to evaluate regression problems where the output (a predicted scalar value) is compared with the true scalar value output for a given data point, making it a good fit for our five star ratings evaluation.

### Cold Start Problem
What if the service aquires a new user? Our model is based off a current user that has a history of ratings within the site, a user has to have a history in order for our model to return recommendations.
To combat this new user issue, known more formally as the Cold Start Problem, we develop two seperate engines that we can incorporate. The first model gives the user the ability to input a move that they subjectively enjoyed in the past. This first model takes a movie title and spits out similar movies based on genres and user defined tags from both their input movie, and the movies in our database. The second model uses Bayesian Upper Confidence Bound Algorithm to determine which movies are the most favourable to recommend to a user without the user having ever seen a movie in their history.

## Summary
In summary our team has developed an ALS movie recommender model using collaborative filtering that will predict the top five movies for a user to view based on ratings by users similar to them. Additionally we developed a content based filtering model that outputs five movies based on a users ratings history. If a user is new to the service they are presented with two options. The first option allows them to input a movie they previously enjoyed and our engine then spits out five movies that user may enjoy. The second option provides a list of five movies from the databse which our model predicts are the most appealing without the user having to input any history.

