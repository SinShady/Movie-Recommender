# Movie-Recommender README.md
![movies](https://i.pinimg.com/originals/55/3a/da/553ada2b9135a3ccdfaaaf31346403dd.png)

# Table of Contents

### Reports
- [Presentation Notebook](https://github.com/SinShady/Movie-Recommender/blob/main/notebooks/final/report.ipynb)
- [Presentation PowerPoint](https://github.com/SinShady/Movie-Recommender/blob/main/reports/Project-4-Presentation.pdf)

### Exploratory Notebooks
- [Sindhu's EDA](https://github.com/SinShady/Movie-Recommender/tree/main/notebooks/exploratory/Sindhu-eda.ipynb)
- [Jeff's EDA](https://github.com/SinShady/Movie-Recommender/blob/main/notebooks/exploratory/Jeff_EDA_small.ipynb)
- [Will's EDA](https://github.com/SinShady/Movie-Recommender/blob/main/notebooks/exploratory/Will_indexs/wills_eda_small.ipynb)

### Helpful Resources
 - [MovieLens Dataset](https://grouplens.org/datasets/movielens/latest/)
 - [How to Install Spark](https://www.datacamp.com/community/tutorials/installation-of-pyspark)

# Business Understanding
In this project, we address the needs of a hypothetical movie streaming business looking to increase revenue. The business is new to online streaming and wants to compete with larger well known online streaming businesses.  Using the <a href="https://grouplens.org/datasets/movielens/latest/">MovieLens dataset</a> and well established data science techniques, we build movie recommendation engines using both collaborative and content based filtering. 

By accurately predicting sound movie recommendations to subscribers, subscribers will stay engaged on streaming platform and remain customers longer. It can also present an opportunity for ad based revenue targeting customers on the platform. Furthermore, satisfied customers are more likely to recommend the streaming service to family and friends. 

# The Data
The data set used for this project is the <a href="https://grouplens.org/datasets/movielens/latest/">MovieLens dataset</a> from the GroupLens research lab at the University of Minnesota. It contains 100,835 unique viewer ratings, 610 individual viewers, and 9,724 movies.

## Preparing the Data
The dataset is a clean dataset containing four CSV files:
1. `links.csv` (9742, 3):
Is a csv file containing 3 columns, `movieId`, `imdbId`, `tmdbId` with 9742 rows. Each row represents a unique movie.
2. `movies.csv` (9742, 3):
Is a csv file containing 3 columns, `movieId`, `title`, and `genre` with 9742 rows. Each row represents a unique movie
3. `ratings.csv` (100836, 4):
Is a csv file containg 4 `columns`, `userId`,	`movieId`, `rating`, `timestamp` with 100836 rows. Each row represents a `rating` from a `userID` assigned to a `movieID`
4. `tags.csv` (3683, 4):
Is a csv file containing 4 columns, `userId`,	`movieId`,	`tag`,	`timestamp` with 2683 rows. Each row represents a `timestamp` a `userID` gave assigned a `movieID` a `tag`.

CSV files are imported and converted to both Pandas and Spark data frames, which are extensively used in this project. Data frames are merged together in advance of modeling on the `movieId` column.

We then use feature engineering to create new features, for example, creating a new column named `liked`. This then re-casts our scores from a 0-5 star rating problem to a binary like/no-like problem, with 4.0 stars and above representing a “liked” movie. Additionally, we have engineered a `genres and tags` column which combines all the genres and user-defined tags per movie.

## Visualization the Data

We can see from this distribution bar chart that the ratings are distrubted normally with a left skew. The most common rating is 4 stars

### <center>Distribution of Ratings</center>

![Ratings Distribution](/reports/figures/ratings_dist.png)

We ordered the movies from most rated to least rated and plotted the rating count per movie to find we had a "long tail" issue. We have strongly skewed ratings with less than 5% of the movies making up most of our rating data. This means that our recommender engine may recommend the most popular movies more, which is not a bad thing as those are the movies people tend to like.

### <center>Amount of Ratings Across all Movies</center>

![Long Tail](/reports/figures/ratings_count_distribution.png)

Below is a word cloud of the genres and user-defined tags in our dataset, each word scaled according to their frequency. We can see that our dataset contains a lot of Drama and Comedy movies.
### <center>Genres and User-Defined Tags</center>

![Genres and Tags](/reports/figures/word_cloud_2.png)

# Recommendation Engines

## Collaborative-Based Filtering
The primary predictive model used in this project is Apache Spark ML Alternating Least Squares (ALS) for collaborative filtering. ALS recommender is a matrix factorization algorithm that uses Alternating Least Squares with Weighted-Lamda-Regularization (ALS-WR). It uses matrix multiplication with user ratings. As there are a lot of blank ratings (not every user has rated every movie), it predicts ratings for those blanks and recommneds movies based on those predictions. Our ALS model predicts top 5 rated movies for each user.  We conduct a train-test split separating data into training and testing sets for model training and evaluation on an 80/20 split respectively. After building our first simple model, and adjusting parameters, we run a param grid to identify the best performing model. We also build custom content based filtering predictive engines using Python. 

### Model Evaluation
Our ALS model is evaluated using the RMSE (Root Mean Squared Error) metric. RMSE or Root Mean Squared Error is used as a measure of prediction accuracy. I.e. Given a set of items (movies) how well can the system predict my ratings for these items, or how well it can predict that i will watch these items. RMSE is typically used to evaluate regression problems where the output (a predicted scalar value) is compared with the true scalar value output for a given data point, making it a good fit for our five star ratings evaluation. 

Our model’s RMSE score is 0.86 which is consistent with other published ALS recommender engines where the same dataset is used. This means, our prediction of what a user might rate a movie vs their actual rating of that movie could vary by an average of .86 and the ratings are on a scale from 1 to 5. This may seem like a big error, but in the grand scale of things, on a ratings matrix of all the movies and all the users, only 98.2% of the matrix is populated. The more data we can train our model with, the more accurate our model will become.


### Example of our Model At Work

![Collab Model Example](/reports/figures/collab_rec_ex.jpg)

## Cold Start Problem
What if the service aquires a new user? Our collaboration-based engine is based off a current user that has a history of ratings within the site. A user has to have a history in order for our model to return recommendations. To combat this new user issue, known more formally as the Cold Start Problem, we develop two seperate engines that we can incorporate.

## Recommendation Engine #2
We created a second recommendation engine which gives the user the ability to input a movie that they subjectively enjoyed in the past. It takes a movie title and spits out similar movies based on genres and user defined tags in our dataset. Here is an example of the engine at work after inputting <i>Eternal Sunshine of the Spotless Mind (2004), 28 Days Later (2002), Kung Fu Panda: Secrets of the Masters (2011), and 10 Things I Hate About You (1999)</i>
![Engine #2](/reports/figures/movie_recs.png)
We can see that our recommendation engine is doing quite well!


## Recommendation Engine #3
What if the user didn't specify any movies they liked? To adress this issue, we created a third recommendation engine which uses Bayesian Upper Confidence Bound Algorithm to determine which movies are the most favourable to recommend to a user without the user having ever seen a movie in their history. This list will self adjust as more movies and ratings get added to the data. The movies recommended using this engine were <i>Mission: Impossible - Fallout (2018), Metal: A Headbanger's Journey (2005), The Deep End of the Ocean (1999), The Program (1993), Take the Lead (2006), Down in the Valley (2005)</i>

## Summary
In summary, our team has developed 3 recommendation engines which can be used for a movie streaming service. We started by creating an ALS movie recommender model using collaborative filtering that will predict the top five movies for a user to view based on ratings by users similar to them. If a user is new to the service, we have presented two options. The first option is to use a content based filtering engine that outputs five movies per title based on a users liked titles while they are signing up for the movie service. The second option provides a list of five movies from the databse which our engine predicts are the most appealing without the user having to input any history. Using all three recommendation engines together, we present multiple options for your recommendation needs. As more movies, users, and ratings get added to the database, the recommendations will only get better.

